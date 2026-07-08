# -*- coding: utf-8 -*-
"""
CellScribe - Streamlit Web Application
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cellscribe.pipeline import CellScribePipeline

# Demo dataset path - LOCAL FILE (no internet download)
DEMO_DATASET = str(Path(__file__).parent.parent / "data" / "sample" / "demo_pbmc.h5ad")


def run_analysis(uploaded_file, min_genes, max_genes, n_top_genes, resolution, use_scvi, use_demo):
    with st.spinner("Running CellScribe pipeline... This may take 1-2 minutes"):
        progress_bar = st.progress(0)
        
        pipeline = CellScribePipeline(output_dir="outputs")
        
        # Load data
        if use_demo:
            st.info("📊 Loading PBMC 3k demo dataset...")
            
            if not Path(DEMO_DATASET).exists():
                st.error("Demo dataset not found at: {}".format(DEMO_DATASET))
                st.info("Please run: python create_demo_data.py")
                return
            
            file_path = DEMO_DATASET
            st.success("✅ Demo data loaded!")
        else:
            # Save uploaded file temporarily
            temp_path = Path("outputs/uploaded_data") / uploaded_file.name
            temp_path.parent.mkdir(parents=True, exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            file_path = str(temp_path)
            st.info("📊 Loaded: {}".format(uploaded_file.name))
        
        progress_bar.progress(10)
        
        # Run pipeline
        try:
            results = pipeline.run_full_pipeline(
                file_path=file_path,
                min_genes=min_genes,
                max_genes=max_genes,
                n_top_genes=n_top_genes,
                resolution=resolution,
                use_scvi=use_scvi,
                annotate=True,
                visualize=True
            )
            
            progress_bar.progress(100)
            st.success("✅ Analysis complete!")
            
            display_results(results, pipeline.adata)
            
        except Exception as e:
            st.error("❌ Error: {}".format(str(e)))
            import traceback
            st.code(traceback.format_exc())


def display_results(results, adata):
    st.header("📊 Analysis Results")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cells", results['qc']['filtered_cells'])
    with col2:
        st.metric("Genes", results['qc']['filtered_genes'])
    with col3:
        st.metric("Clusters", results['clustering']['n_clusters'])
    with col4:
        if 'annotation' in results:
            st.metric("Cell Types", len(results['annotation']['cell_types']))
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 QC Metrics", "🗺️ UMAP", "🧬 Cell Types", "📊 DE Analysis", "📥 Download"])
    
    with tab1:
        st.subheader("Quality Control")
        if 'plots' in results and 'qc_metrics' in results['plots']:
            st.image(results['plots']['qc_metrics'], use_container_width=True)
        elif 'plots' in results and 'qc' in results['plots']:
            st.image(results['plots']['qc'], use_container_width=True)
        
        # QC table
        qc_df = pd.DataFrame({
            'Metric': ['Original Cells', 'Filtered Cells', 'Original Genes', 'Filtered Genes'],
            'Count': [
                results['qc']['original_cells'],
                results['qc']['filtered_cells'],
                results['qc']['original_genes'],
                results['qc']['filtered_genes']
            ]
        })
        st.dataframe(qc_df, use_container_width=True)
    
    with tab2:
        st.subheader("UMAP Visualization")
        col1, col2 = st.columns(2)
        with col1:
            if 'plots' in results and 'umap_clusters' in results['plots']:
                st.image(results['plots']['umap_clusters'], caption="Clusters & Cell Types", use_container_width=True)
        with col2:
            # Show cell type distribution on UMAP if available
            if 'cell_type' in adata.obs.columns:
                st.write("**Cell Type Distribution**")
                cell_type_counts = adata.obs['cell_type'].value_counts()
                st.bar_chart(cell_type_counts)
    
    with tab3:
        st.subheader("Cell Type Annotation")
        if 'annotation' in results:
            annotation = results['annotation']
            st.write("**Method:** {}".format(annotation['method']))
            
            # Handle mean_confidence safely
            mean_conf = annotation.get('mean_confidence', 'N/A')
            if isinstance(mean_conf, float):
                st.write("**Mean Confidence:** {:.3f}".format(mean_conf))
            else:
                st.write("**Mean Confidence:** {}".format(mean_conf))
            
            # Cell type counts - handle both dict and list formats
            cell_counts = annotation.get('cell_counts', {})
            if cell_counts:
                cell_types_df = pd.DataFrame({
                    'Cell Type': list(cell_counts.keys()),
                    'Count': list(cell_counts.values())
                }).sort_values('Count', ascending=False)
                
                st.dataframe(cell_types_df, use_container_width=True)
                st.bar_chart(cell_types_df.set_index('Cell Type'))
            else:
                # Fallback: count from adata
                cell_type_counts = adata.obs['cell_type'].value_counts().reset_index()
                cell_type_counts.columns = ['Cell Type', 'Count']
                st.dataframe(cell_type_counts, use_container_width=True)
                st.bar_chart(cell_type_counts.set_index('Cell Type'))
        else:
            st.info("No annotation results available.")
    
    with tab4:
        st.subheader("Differential Expression")
        if 'de_analysis' in results:
            if results['de_analysis'].get('n_groups', 0) == 0:
                st.warning("DE analysis skipped: Some cell types had too few cells for statistical comparison.")
                st.info("This is normal for rare cell types. The annotation still worked correctly.")
            else:
                st.write("Analyzed {} groups".format(results['de_analysis']['n_groups']))
                
                # Select group to view
                groups = results['de_analysis'].get('groups', [])
                if groups:
                    group = st.selectbox("Select cell type", groups)
                    
                    # Load and display DE results
                    safe_name = group.replace(' ', '_').replace('/', '_').replace('+', 'pos')
                    de_file = "outputs/de_{}.csv".format(safe_name)
                    if Path(de_file).exists():
                        de_df = pd.read_csv(de_file)
                        if de_df.empty:
                            st.warning("No DE results available for this group.")
                        else:
                            st.dataframe(de_df.head(20), use_container_width=True)
                        
                        # Volcano plot
                        if not de_df.empty and 'logfoldchanges' in de_df.columns:
                            fig, ax = plt.subplots(figsize=(10, 6))
                            
                            # Clean data - remove NaN values
                            clean_df = de_df.dropna(subset=['logfoldchanges', 'pvals_adj', 'scores'])
                            
                            if len(clean_df) == 0:
                                st.warning("No valid data points for volcano plot after removing NaN values.")
                            else:
                                # Replace 0 p-values with very small number
                                pvals_clean = clean_df['pvals_adj'].replace(0, 1e-300)
                                
                                scatter = ax.scatter(
                                    clean_df['logfoldchanges'], 
                                    -np.log10(pvals_clean),
                                    c=clean_df['scores'],
                                    cmap='viridis',
                                    alpha=0.6,
                                    edgecolors='none'
                                )
                                ax.set_xlabel('Log2 Fold Change')
                                ax.set_ylabel('-Log10 Adjusted P-value')
                                ax.set_title('DE Genes: {}'.format(group))
                                ax.axhline(y=-np.log10(0.05), color='r', linestyle='--', label='p=0.05')
                                ax.legend()
                                plt.colorbar(scatter, label='Score')
                                st.pyplot(fig)
                    else:
                        st.warning("DE file not found: {}".format(de_file))
        else:
            st.info("DE analysis not available.")
    
    with tab5:
        st.subheader("Download Results")
        
        # Download processed data
        if Path(results['output_path']).exists():
            with open(results['output_path'], "rb") as f:
                st.download_button(
                    "📥 Download Processed Data (.h5ad)",
                    f,
                    file_name="cellscribe_results.h5ad",
                    mime="application/octet-stream"
                )
        
        # Download plots
        if 'plots' in results:
            for plot_name, plot_path in results['plots'].items():
                if plot_path.endswith('.png') and Path(plot_path).exists():
                    with open(plot_path, "rb") as f:
                        st.download_button(
                            "📥 Download {}".format(plot_name),
                            f,
                            file_name="{}.png".format(plot_name),
                            mime="image/png"
                        )


def main():
    st.set_page_config(
        page_title="CellScribe",
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Single clean header
    st.title("🧬 CellScribe")
    st.caption("Automated Single-Cell RNA-seq Analysis & Cell Type Annotation")
    st.markdown("---")
    
    st.sidebar.header("📁 Upload Data")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader(
        "Upload single-cell data",
        type=['h5ad', 'h5', 'mtx', 'csv'],
        help="Supported: .h5ad, .h5 (10x), .mtx (Matrix Market), .csv"
    )
    
    # Parameters
    st.sidebar.header("⚙️ Parameters")
    min_genes = st.sidebar.slider("Min genes per cell", 50, 1000, 200)
    max_genes = st.sidebar.slider("Max genes per cell", 1000, 15000, 8000)
    n_top_genes = st.sidebar.slider("Highly variable genes", 500, 5000, 2000)
    resolution = st.sidebar.slider("Clustering resolution", 0.1, 2.0, 1.0, 0.1)
    use_scvi = st.sidebar.checkbox("Use scVI batch correction", value=False)
    
    # Demo data option
    use_demo = st.sidebar.checkbox("Use demo data (PBMC 3k)", value=False)
    
    if uploaded_file or use_demo:
        run_analysis(uploaded_file, min_genes, max_genes, n_top_genes, resolution, use_scvi, use_demo)


if __name__ == "__main__":
    main()