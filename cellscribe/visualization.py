"""
CellScribe - Visualization Utilities
"""

import scanpy as sc
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class CellScribeVisualizer:
    """Generate publication-ready plots for single-cell analysis."""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def plot_qc_metrics(self, adata, save: bool = True) -> str:
        """Plot QC metrics."""
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        sc.pl.violin(adata, ['n_genes_by_counts'], jitter=0.4, ax=axes[0], show=False)
        axes[0].set_title('Genes per Cell')
        
        sc.pl.violin(adata, ['total_counts'], jitter=0.4, ax=axes[1], show=False)
        axes[1].set_title('Total Counts per Cell')
        
        sc.pl.violin(adata, ['pct_counts_mt'], jitter=0.4, ax=axes[2], show=False)
        axes[2].set_title('Mitochondrial %')
        
        plt.tight_layout()
        
        if save:
            path = self.output_dir / "qc_metrics.png"
            plt.savefig(path, dpi=300, bbox_inches='tight')
            logger.info(f"Saved QC plot to {path}")
            plt.close()
            return str(path)
        plt.show()
        return None
    
    def plot_umap(self, adata, color_by: str = 'leiden', save: bool = True) -> str:
        """Plot UMAP with clusters or cell types."""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sc.pl.umap(adata, color=color_by, legend_loc='on data', 
                  legend_fontsize=12, ax=ax, show=False,
                  title=f'UMAP colored by {color_by}')
        
        plt.tight_layout()
        
        if save:
            path = self.output_dir / f"umap_{color_by}.png"
            plt.savefig(path, dpi=300, bbox_inches='tight')
            logger.info(f"Saved UMAP plot to {path}")
            plt.close()
            return str(path)
        plt.show()
        return None
    
    def plot_cell_types(self, adata, save: bool = True) -> str:
        """Plot cell type distribution."""
        cell_counts = adata.obs['cell_type'].value_counts()
        
        fig = px.pie(
            values=cell_counts.values,
            names=cell_counts.index,
            title='Cell Type Distribution',
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        
        if save:
            path = self.output_dir / "cell_types_pie.html"
            fig.write_html(path)
            logger.info(f"Saved cell type plot to {path}")
            return str(path)
        fig.show()
        return None
    
    def generate_report(self, adata, results: dict) -> dict:
        """Generate all plots and return paths."""
        logger.info("Generating visualization report...")
        
        plots = {}
        
        # QC metrics
        if 'qc' in results:
            plots['qc'] = self.plot_qc_metrics(adata)
        
        # UMAP clusters
        plots['umap_clusters'] = self.plot_umap(adata, color_by='leiden')
        
        # UMAP cell types (if available)
        if 'cell_type' in adata.obs.columns:
            plots['umap_cell_types'] = self.plot_umap(adata, color_by='cell_type')
            plots['cell_types'] = self.plot_cell_types(adata)
        
        logger.info(f"Generated {len(plots)} plots")
        return plots