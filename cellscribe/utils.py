"""
CellScribe - Utility Functions
"""

import logging
from pathlib import Path
from typing import Dict, Any
import json

def setup_logging(level: int = logging.INFO):
    """Setup logging configuration."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def save_results_summary(results: Dict[str, Any], output_path: str):
    """Save results summary as JSON."""
    # Remove non-serializable objects
    summary = {k: v for k, v in results.items() if k not in ['adata', 'scvi']}
    
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    
    return str(path)