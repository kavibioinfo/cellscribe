"""
CellScribe - Single-Cell RNA-seq Automated Analysis Pipeline
"""

import scanpy as sc
import anndata
import numpy as np
import pandas as pd
from pathlib import Path
import warnings
from typing import Optional, Dict, List, Tuple
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CellScribePipeline:
    """
    Automated single-cell RNA-seq analysis pipeline.
    """
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.adata: Optional[anndata.AnnData] = None
        self.results: Dict = {}
        
    def load_data(self, file_path: str, **kwargs) -> anndata.AnnData:
        path = Path(file_path)
        logger.info(f"Loading data from {path}")
        
        if path.suffix == '.h5ad':
            self.adata = sc.read_h5ad(path)
        elif path.suffix == '.h5':
            self.adata = sc.read_10x_h5(path)
        elif path.suffix == '.mtx':
            self.adata = sc.read_mtx(path).T
    
            parent_dir = path.parent
            genes_file = parent_dir / 'genes.tsv'
            barcodes_file = parent_dir / 'barcodes.tsv'
    
            if genes_file.exists():
                genes = pd.read_csv(genes_file, sep='\t', header=None)
                if genes.shape[1] >= 2:
                    self.adata.var_names = genes[1].values
                    self.adata.var['gene_id'] = genes[0].values
                    logger.info("Using gene symbols as var_names")
                else:
                    self.adata.var_names = genes[0].values
                logger.info(f"Loaded {len(genes)} gene names from {genes_file}")
    
            if barcodes_file.exists():
                barcodes = pd.read_csv(barcodes_file, sep='\t', header=None)
                self.adata.obs_names = barcodes[0].values
                logger.info(f"Loaded {len(barcodes)} barcodes from {barcodes_file}")
    
            # Make gene names unique BEFORE any processing
            self.adata.var_names_make_unique()
            logger.info("Made gene names unique")
        return self.adata
    
    def qc_filter(self, 
                  min_genes: int = 200,
                  max_genes: int = 8000,
                  min_cells: int = 3,
                  max_mt_percent: float = 20.0,
                  min_counts: int = 100) -> anndata.AnnData:
        logger.info("Running QC filtering...")
        
        self.adata.var['mt'] = self.adata.var_names.str.startswith('MT-')
        sc.pp.calculate_qc_metrics(self.adata, qc_vars=['mt'], inplace=True)
        
        original_cells = self.adata.n_obs
        original_genes = self.adata.n_vars
        
        self.adata = self.adata[
            (self.adata.obs.n_genes_by_counts >= min_genes) &
            (self.adata.obs.n_genes_by_counts <= max_genes) &
            (self.adata.obs.pct_counts_mt <= max_mt_percent) &
            (self.adata.obs.total_counts >= min_counts)
        ].copy()
        
        sc.pp.filter_genes(self.adata, min_cells=min_cells)
        
        filtered_cells = self.adata.n_obs
        filtered_genes = self.adata.n_vars
        
        logger.info(f"QC: {original_cells} -> {filtered_cells} cells, "
                    f"{original_genes} -> {filtered_genes} genes")
        
        self.results['qc'] = {
            'original_cells': original_cells,
            'filtered_cells': filtered_cells,
            'original_genes': original_genes,
            'filtered_genes': filtered_genes
        }
        
        return self.adata
    
    def normalize_and_scale(self, target_sum: float = 1e4) -> anndata.AnnData:
        logger.info("Normalizing and scaling...")
        sc.pp.normalize_total(self.adata, target_sum=target_sum)
        sc.pp.log1p(self.adata)
        self.adata.raw = self.adata.copy()
        logger.info("Normalization complete")
        return self.adata
    
    def select_features(self, n_top_genes: int = 2000) -> anndata.AnnData:
        logger.info(f"Selecting top {n_top_genes} highly variable genes...")
        sc.pp.highly_variable_genes(self.adata, n_top_genes=n_top_genes)
        logger.info(f"Selected {self.adata.var.highly_variable.sum()} HVGs")
        return self.adata
    
    def reduce_dimensions(self, n_comps: int = 50) -> anndata.AnnData:
        logger.info("Running PCA...")
        
        if hasattr(self.adata.X, 'toarray'):
            self.adata.X = self.adata.X.toarray()
        
        sc.pp.scale(self.adata)
        sc.tl.pca(self.adata, n_comps=n_comps, svd_solver='arpack')
        sc.pp.neighbors(self.adata, n_neighbors=15, n_pcs=30)
        
        logger.info("Dimensionality reduction complete")
        return self.adata
    
    def run_scvi(self, batch_key: Optional[str] = None) -> anndata.AnnData:
        try:
            import scvi
            logger.info("Running scVI batch correction...")
            
            scvi.model.SCVI.setup_anndata(self.adata, batch_key=batch_key)
            vae = scvi.model.SCVI(self.adata, n_layers=2, n_latent=30)
            vae.train(max_epochs=100, early_stopping=True)
            
            self.adata.obsm['X_scVI'] = vae.get_latent_representation()
            sc.pp.neighbors(self.adata, use_rep='X_scVI')
            
            logger.info("scVI batch correction complete")
            self.results['scvi'] = {'model': vae, 'latent_dim': 30, 'trained': True}
            
        except Exception as e:
            logger.warning(f"scVI failed: {e}. Falling back to PCA neighbors.")
            
        return self.adata
    
    def cluster(self, resolution: float = 1.0) -> anndata.AnnData:
        logger.info("Clustering with Leiden algorithm...")
        
        sc.tl.leiden(self.adata, resolution=resolution, flavor="igraph", n_iterations=2, directed=False)
        sc.tl.umap(self.adata)
        
        n_clusters = self.adata.obs['leiden'].nunique()
        logger.info(f"Found {n_clusters} clusters")
        
        self.results['clustering'] = {
            'n_clusters': n_clusters,
            'resolution': resolution
        }
        
        return self.adata
    
    def annotate_cells(self, method: str = 'auto', model: Optional[str] = None) -> Dict:
        from cellscribe.annotation import CellTypeAnnotator
        
        logger.info("Annotating cell types...")
        annotator = CellTypeAnnotator()
        annotation_results = annotator.annotate(self.adata, method=method, model=model)
        
        self.results['annotation'] = annotation_results
        logger.info(f"Annotation complete: {annotation_results['method']}")
        
        return annotation_results
    
    def generate_visualizations(self) -> Dict:
        from cellscribe.visualization import CellScribeVisualizer
        
        visualizer = CellScribeVisualizer(str(self.output_dir))
        plots = visualizer.generate_report(self.adata, self.results)
        self.results['plots'] = plots
        return plots

    def run_de_analysis(self, groupby: str = 'cell_type') -> Dict:
        """Run differential expression analysis."""
        from cellscribe.de_analysis import DEAnalyzer
        
        logger.info("Running differential expression analysis...")
        analyzer = DEAnalyzer(self.adata)
        de_results = analyzer.run_de(groupby=groupby)
        
        if not de_results:
            logger.warning("DE analysis returned no results")
            self.results['de_analysis'] = {
                'groups': [],
                'n_groups': 0,
                'skipped': 'Insufficient cells per group'
            }
            return {}
        
        self.results['de_analysis'] = {
            'groups': list(de_results.keys()),
            'n_groups': len(de_results)
        }
        
        # Save DE results
        for group, df in de_results.items():
            safe_name = group.replace(' ', '_').replace('/', '_').replace('+', 'pos')
            output_path = self.output_dir / f"de_{safe_name}.csv"
            df.to_csv(output_path, index=False)
            
        logger.info("DE analysis complete")        
        return de_results
    
    def run_full_pipeline(self, 
                          file_path: str,
                          min_genes: int = 200,
                          max_genes: int = 8000,
                          n_top_genes: int = 2000,
                          resolution: float = 1.0,
                          use_scvi: bool = True,
                          batch_key: Optional[str] = None,
                          annotate: bool = True,
                          visualize: bool = True) -> Dict:
        logger.info("=" * 50)
        logger.info("STARTING CELLSCRIBE PIPELINE")
        logger.info("=" * 50)
        
        self.load_data(file_path)
        self.qc_filter(min_genes=min_genes, max_genes=max_genes)
        self.normalize_and_scale()
        self.select_features(n_top_genes=n_top_genes)
        self.reduce_dimensions()
        
        if use_scvi:
            self.run_scvi(batch_key=batch_key)
        
        self.cluster(resolution=resolution)
        
        if annotate:
            self.annotate_cells(method='auto')
            self.run_de_analysis(groupby='cell_type')
        
        if visualize:
            self.generate_visualizations()
            
        if hasattr(self.adata.X, 'toarray'):
            data_check = self.adata.X.toarray()
        else:
            data_check = self.adata.X
        
        # If data has negative values or NaN, it's likely already log-normalized
        has_negative = (data_check < 0).any() if hasattr(data_check, 'any') else False
        has_nan = np.isnan(data_check).any() if hasattr(data_check, 'any') else False
        
        if has_negative or has_nan:
            logger.warning("Data appears to be pre-processed. Skipping normalization.")
            # Store raw if not already stored
            if self.adata.raw is None:
                self.adata.raw = self.adata.copy()
        else:
            # Step 3: Normalize (only if raw counts)
            self.normalize_and_scale()
        
        # Step 4: Feature selection (always run)
        self.select_features(n_top_genes=n_top_genes)
        
        output_path = self.output_dir / "processed_data.h5ad"
        self.adata.write(output_path)
        logger.info(f"Saved processed data to {output_path}")
        
        self.results['output_path'] = str(output_path)
        self.results['adata'] = self.adata
        
        logger.info("=" * 50)
        logger.info("PIPELINE COMPLETE")
        logger.info("=" * 50)
        
        return self.results


def run_cellscribe(file_path: str, **kwargs) -> Dict:
    pipeline = CellScribePipeline()
    return pipeline.run_full_pipeline(file_path, **kwargs)