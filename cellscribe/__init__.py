"""
CellScribe - Single-Cell RNA-seq Automated Analysis
"""

from .pipeline import CellScribePipeline, run_cellscribe
from .annotation import CellTypeAnnotator
from .visualization import CellScribeVisualizer

__version__ = "0.1.0"
__all__ = ["CellScribePipeline", "run_cellscribe", "CellTypeAnnotator", "CellScribeVisualizer"]