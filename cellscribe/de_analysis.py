"""
CellScribe - Differential Expression Analysis
"""

import scanpy as sc
import pandas as pd
import numpy as np
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class DEAnalyzer:
    """Differential expression analysis between cell types or clusters."""
    
    def __init__(self, adata):
        self.adata = adata
        
    def run_de(self, groupby: str = 'cell_type', method: str = 'wilcoxon', min_cells: int = 3) -> Dict[str, pd.DataFrame]:
        """
        Run differential expression for each group.
        Only analyzes groups with at least min_cells cells.
        """
        logger.info(f"Running DE analysis by {groupby} using {method}...")
        
        # Check cell counts per group
        cell_counts = self.adata.obs[groupby].value_counts()
        valid_groups = cell_counts[cell_counts >= min_cells].index.tolist()
        skipped_groups = cell_counts[cell_counts < min_cells].index.tolist()
        
        if skipped_groups:
            logger.warning(f"Skipping groups with < {min_cells} cells: {skipped_groups}")
        
        if len(valid_groups) < 2:
            logger.warning("Not enough groups for DE analysis (need at least 2)")
            return {}
        
        # Filter to valid groups only
        adata_filtered = self.adata[self.adata.obs[groupby].isin(valid_groups)].copy()
        
        # Reorder categories to remove empty ones
        adata_filtered.obs[groupby] = adata_filtered.obs[groupby].cat.remove_unused_categories()
        
        sc.tl.rank_genes_groups(
            adata_filtered, 
            groupby=groupby, 
            method=method,
            corr_method='benjamini-hochberg'
        )
        
        # Extract results for each group
        results = {}
        groups = adata_filtered.obs[groupby].cat.categories
        
        for group in groups:
            df = sc.get.rank_genes_groups_df(adata_filtered, group=group)
            df = df.head(50)
            results[group] = df
        
        logger.info(f"DE analysis complete for {len(groups)} groups")
        return results