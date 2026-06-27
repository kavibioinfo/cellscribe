"""
CellScribe - Automated Cell Type Annotation
"""

import scanpy as sc
import logging
from typing import Dict, Optional
import warnings

logger = logging.getLogger(__name__)

class CellTypeAnnotator:
    """
    Automated cell type annotation using CellTypist.
    Falls back to marker-based annotation if CellTypist fails.
    """
    
    def __init__(self):
        self.predictions = None
        self.confidence_scores = None
        
    def annotate_with_celltypist(self, adata, model: str = 'Immune_All_Low.pkl') -> Dict:
        """
        Annotate cells using CellTypist pre-trained models.
        """
        try:
            import celltypist
            from celltypist import models
            
            logger.info(f"Running CellTypist with model: {model}")
            
            # Download model if not present
            models.download_models(model=model)
            
            # Predict cell types
            predictions = celltypist.annotate(
                adata, 
                model=model,
                majority_voting=True
            )
            
            # Add predictions to adata
            adata.obs['cell_type'] = predictions.predicted_labels.predicted_labels
            adata.obs['cell_type_confidence'] = predictions.probability_matrix.max(axis=1)
            
            # Store results
            self.predictions = predictions
            self.confidence_scores = adata.obs['cell_type_confidence']
            
            # Summary
            cell_type_counts = adata.obs['cell_type'].value_counts().to_dict()
            logger.info(f"Annotated {len(cell_type_counts)} cell types")
            logger.info(f"Top cell types: {list(cell_type_counts.keys())[:5]}")
            
            return {
                'method': 'celltypist',
                'model': model,
                'cell_types': cell_type_counts,
                'mean_confidence': float(adata.obs['cell_type_confidence'].mean()),
                'adata': adata
            }
            
        except Exception as e:
            logger.warning(f"CellTypist failed: {e}")
            logger.info("Falling back to marker-based annotation...")
            return self.annotate_with_markers(adata)
    
    def annotate_with_markers(self, adata) -> Dict:
        """
        Simple marker-based annotation for PBMC data.
        Uses known markers for major immune cell types.
        Handles missing genes gracefully.
        """
        logger.info("Running marker-based annotation...")
        
        # Define markers for PBMC cell types
        markers = {
            'CD14+ Monocytes': ['CD14', 'LYZ', 'S100A9', 'S100A8', 'FCGR3A'],
            'CD4 T cells': ['IL7R', 'CD4', 'LTB', 'TRAC', 'TRBC1'],
            'CD8 T cells': ['CD8A', 'CD8B', 'GZMK', 'GZMA', 'CCL5'],
            'B cells': ['CD79A', 'MS4A1', 'CD79B', 'IGHM', 'IGHD'],
            'NK cells': ['GNLY', 'NKG7', 'KLRD1', 'GZMB', 'PRF1'],
            'FCGR3A+ Monocytes': ['FCGR3A', 'MS4A7', 'VMO1', 'LYZ', 'S100A8'],
            'Dendritic cells': ['FCER1A', 'CST3', 'CLEC10A', 'IRF8', 'CD1C'],
            'Megakaryocytes': ['PPBP', 'PF4', 'GNG11', 'ITGA2B', 'GP9'],
            'Platelets': ['PPBP', 'PF4', 'GNG11'],
            'Erythrocytes': ['HBA1', 'HBA2', 'HBB', 'ALAS2']
        }
        
        # Get available genes in dataset
        available_genes = set(adata.var_names)
        logger.info(f"Dataset has {len(available_genes)} genes")
        
        # Score each cell type with available markers only
        scored_cell_types = {}
        
        for cell_type, gene_list in markers.items():
            # Find which markers exist in the dataset
            valid_genes = [g for g in gene_list if g in available_genes]
            
            if len(valid_genes) >= 2:  # Need at least 2 genes to score
                try:
                    score_name = f"score_{cell_type.replace(' ', '_').replace('+', 'pos')}"
                    sc.tl.score_genes(adata, gene_list=valid_genes, score_name=score_name)
                    scored_cell_types[cell_type] = score_name
                    logger.info(f"  {cell_type}: scored with {len(valid_genes)}/{len(gene_list)} markers")
                except Exception as e:
                    logger.warning(f"  {cell_type}: scoring failed - {e}")
            else:
                logger.warning(f"  {cell_type}: skipped (only {len(valid_genes)}/{len(gene_list)} markers found)")
        
        if not scored_cell_types:
            logger.warning("No valid markers found! Using cluster IDs as cell types.")
            adata.obs['cell_type'] = 'Cluster_' + adata.obs['leiden'].astype(str)
            adata.obs['cell_type_confidence'] = 0.5
            
            cell_type_counts = adata.obs['cell_type'].value_counts().to_dict()
            return {
                'method': 'cluster_fallback',
                'cell_types': cell_type_counts,
                'mean_confidence': 0.5,
                'adata': adata
            }
        
        # Assign cell type based on highest score
        score_cols = list(scored_cell_types.values())
        scores = adata.obs[score_cols]
        
        # Map score column names back to cell types
        score_to_celltype = {v: k for k, v in scored_cell_types.items()}
        
        # Get the cell type with highest score for each cell
        adata.obs['cell_type'] = scores.idxmax(axis=1).map(score_to_celltype)
        adata.obs['cell_type_confidence'] = scores.max(axis=1)
        
        # Normalize confidence to 0-1 range
        conf_min = adata.obs['cell_type_confidence'].min()
        conf_max = adata.obs['cell_type_confidence'].max()
        if conf_max > conf_min:
            adata.obs['cell_type_confidence'] = (adata.obs['cell_type_confidence'] - conf_min) / (conf_max - conf_min)
        else:
            adata.obs['cell_type_confidence'] = 0.5
        
        cell_type_counts = adata.obs['cell_type'].value_counts().to_dict()
        logger.info(f"Annotated {len(cell_type_counts)} cell types")
        logger.info(f"Top cell types: {list(cell_type_counts.keys())[:5]}")
        
        return {
            'method': 'marker_based',
            'cell_types': cell_type_counts,
            'mean_confidence': float(adata.obs['cell_type_confidence'].mean()),
            'adata': adata
        }
    
    def annotate(self, adata, method: str = 'auto', model: Optional[str] = None) -> Dict:
        """
        Main annotation method.
        
        Args:
            adata: AnnData object with processed data
            method: 'celltypist', 'markers', or 'auto' (tries celltypist first)
            model: CellTypist model name (if using celltypist)
        """
        if method == 'celltypist':
            return self.annotate_with_celltypist(adata, model or 'Immune_All_Low.pkl')
        elif method == 'markers':
            return self.annotate_with_markers(adata)
        else:
            # Auto: try CellTypist first, fall back to markers
            return self.annotate_with_celltypist(adata, model or 'Immune_All_Low.pkl')