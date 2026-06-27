import sys
sys.path.insert(0, 'H:\\Projects\\cellscribe')

from cellscribe.pipeline import run_cellscribe

print("=" * 60)
print("CELLSCRIBE PIPELINE TEST")
print("=" * 60)

results = run_cellscribe(
    file_path="data/sample/filtered_gene_bc_matrices/hg19/matrix.mtx",
    min_genes=200,
    max_genes=8000,
    use_scvi=False,
    annotate=True  # Enable annotation
)

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Output saved to: {results['output_path']}")
print(f"Clusters found: {results['clustering']['n_clusters']}")
print(f"Cells after QC: {results['qc']['filtered_cells']}")
print(f"Genes after QC: {results['qc']['filtered_genes']}")

if 'annotation' in results:
    print(f"\nAnnotation method: {results['annotation']['method']}")
    print(f"Cell types found: {list(results['annotation']['cell_types'].keys())[:5]}")
    print(f"Mean confidence: {results['annotation']['mean_confidence']:.3f}")

print("=" * 60)