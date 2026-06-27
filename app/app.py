"""
CellScribe - Streamlit Web Application
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from cellscribe.pipeline import CellScribePipeline

st.set_page_config(
    page_title="CellScribe",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="main-header">🧬 CellScribe</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Automated Single-Cell RNA-seq Analysis & Cell Type Annotation</p>', unsafe_allow_html=True)
    
    st.sidebar.header("📁 Upload Data")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader(
        "Upload single-cell data",
        type=['h5ad', 'h5', 'mtx', 'csv'],
        help="Supported: .h5ad, .h5 (10x), .mtx (Matrix Market), .csv"
    )
    
    # Parameters
    st.sidebar.header("⚙️ Parameters")
    min_genes = st.sidebar.slider("Min genes per cell", 100, 1000, 200)
    max_genes = st.sidebar.slider("Max genes per cell", 5000, 15000, 8000)
    n_top_genes = st.sidebar.slider("Highly variable genes", 1000, 5000, 2000)
    resolution = st.sidebar.slider("Clustering resolution", 0.1, 2.0, 1.0, 0.1)
    use_scvi = st.sidebar.checkbox("Use scVI batch correction", value=False)
    
    # Demo data option
    use_demo = st.sidebar.checkbox("Use demo data (PBMC 3k)", value=False)
    
    if uploaded_file or use_demo:
        run_analysis(uploaded_file, min_genes, max_genes, n_top_genes, resolution, use_scvi, use_demo)

def run_analysis(uploaded_file, min_genes, max_genes, n_top_genes, resolution, use_scvi, use_demo):
    with st.spinner("Running CellScribe pipeline..."):
        progress_bar = st.progress(0)
        
        pipeline = CellScribePipeline(output_dir="outputs")
        
        # Load data
        if use_demo:
            st.info("📊 Loading PBMC 3k demo dataset from scanpy...")
            import scanpy as sc
    
            # Download built-in dataset (cached after first run)
            @st.cache_data
            def load_pbmc_demo():
                adata = sc.datasets.pbmc3k()
                # Save temporarily for pipeline
                temp_path = Path("outputs/demo_data.h5ad")
                temp_path.parent.mkdir(parents=True, exist_ok=True)
                adata.write(temp_path)
                return str(temp_path)
    
            file_path = load_pbmc_demo()
            st.success("✅ Demo data loaded!")
        else:
            # Save uploaded file temporarily
            temp_path = Path("outputs/uploaded_data") / uploaded_file.name
            temp_path.parent.mkdir(parents=True, exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            file_path = str(temp_path)
            st.info(f"📊 Loaded: {uploaded_file.name}")
        
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
            st.error(f"❌ Error: {str(e)}")
            raise

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
        if 'plots' in results and 'qc' in results['plots']:
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
                st.image(results['plots']['umap_clusters'], caption="Clusters", use_container_width=True)
        with col2:
            if 'plots' in results and 'umap_cell_types' in results['plots']:
                st.image(results['plots']['umap_cell_types'], caption="Cell Types", use_container_width=True)
    
    with tab3:
        st.subheader("Cell Type Annotation")
        if 'annotation' in results:
            annotation = results['annotation']
            st.write(f"**Method:** {annotation['method']}")
            st.write(f"**Mean Confidence:** {annotation['mean_confidence']:.3f}")
            
            # Cell type counts
            cell_types_df = pd.DataFrame({
                'Cell Type': list(annotation['cell_types'].keys()),
                'Count': list(annotation['cell_types'].values())
            }).sort_values('Count', ascending=False)
            
            st.dataframe(cell_types_df, use_container_width=True)
            
            # Bar chart
            st.bar_chart(cell_types_df.set_index('Cell Type'))
            
            # Pie chart
            if 'plots' in results and 'cell_types' in results['plots']:
                with open(results['plots']['cell_types'], 'r', encoding='utf-8') as f:
                    html_content = f.read()
                st.components.v1.html(html_content, height=600)
    
    with tab4:
        st.subheader("Differential Expression")
        if 'de_analysis' in results:
            if results['de_analysis']['n_groups'] == 0:
                st.warning("DE analysis skipped: Some cell types had too few cells for statistical comparison.")
                st.info("This is normal for rare cell types. The annotation still worked correctly.")
            else:
                st.write(f"Analyzed {results['de_analysis']['n_groups']} groups")
                
                # Select group to view
                group = st.selectbox("Select cell type", results['de_analysis']['groups'])
                
                # Load and display DE results
                safe_name = group.replace(' ', '_').replace('/', '_').replace('+', 'pos')
                de_file = f"outputs/de_{safe_name}.csv"
                if Path(de_file).exists():
                    de_df = pd.read_csv(de_file)
                    st.dataframe(de_df.head(20), use_container_width=True)
                    
                    # Volcano plot
                    fig, ax = plt.subplots(figsize=(10, 6))
                    pvals_adj = de_df['pvals_adj'].replace(0, 1e-300)
                    scatter = ax.scatter(
                        de_df['logfoldchanges'], 
                        -np.log10(pvals_adj),
                        c=de_df['scores'],
                        cmap='viridis',
                        alpha=0.6
                    )
                    ax.set_xlabel('Log2 Fold Change')
                    ax.set_ylabel('-Log10 Adjusted P-value')
                    ax.set_title(f'DE Genes: {group}')
                    ax.axhline(y=-np.log10(0.05), color='r', linestyle='--', label='p=0.05')
                    ax.legend()
                    plt.colorbar(scatter, label='Score')
                    st.pyplot(fig)
        else:
            st.info("DE analysis not available.")
    
    with tab5:
        st.subheader("Download Results")
        
        # Download processed data
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
                if plot_path.endswith('.png'):
                    with open(plot_path, "rb") as f:
                        st.download_button(
                            f"📥 Download {plot_name}",
                            f,
                            file_name=f"{plot_name}.png",
                            mime="image/png"
                        )

if __name__ == "__main__":
    main()