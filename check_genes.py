import scanpy as sc

# Load the processed data
adata = sc.read_h5ad("outputs/processed_data.h5ad")

print("First 20 gene names:")
print(adata.var_names[:20].tolist())

print("\nTotal genes:", adata.n_vars)

# Check if common markers exist
markers = ['CD14', 'LYZ', 'IL7R', 'CD4', 'CD8A', 'CD79A', 'MS4A1', 'GNLY', 'NKG7', 'PPBP']
print("\nChecking common markers:")
for marker in markers:
    if marker in adata.var_names:
        print(f"  ✓ {marker} - FOUND")
    else:
        print(f"  ✗ {marker} - NOT FOUND")