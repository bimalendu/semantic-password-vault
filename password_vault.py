import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Initialize model (use a lightweight one for speed)
@st.cache_resource
def get_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# Load CSV
def load_csv(file):
    df = pd.read_csv(file)
    expected_cols = ['name', 'url', 'username', 'password']
    
    # Try to infer correct columns
    for col in expected_cols:
        if col not in df.columns:
            lower_cols = [c.lower() for c in df.columns]
            if col in lower_cols:
                df.rename(columns={df.columns[lower_cols.index(col)]: col}, inplace=True)
    
    # Drop rows without URL or username
    df.dropna(subset=['url', 'username'], inplace=True)
    
    return df

# Prepare searchable text
def create_search_corpus(df):
    return (df['url'] + " " + df['username']).tolist()

# Streamlit UI
st.set_page_config(page_title="Password Semantic Search", layout="centered")
st.title("🔐 Semantic Password Vault (Offline & Safe)")

uploaded_file = st.file_uploader("Upload your exported password CSV file", type=["csv"])

if uploaded_file:
    try:
        df = load_csv(uploaded_file)
        st.success(f"Loaded {len(df)} credentials.")

        # Semantic search setup
        model = get_model()
        corpus = create_search_corpus(df)
        corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

        # Search input
        search_query = st.text_input("🔍 Enter search (website, username, etc.):")

        if search_query:
            query_embedding = model.encode(search_query, convert_to_tensor=True)
            hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=len(df))[0]

            # Load more functionality
            if 'visible_hits' not in st.session_state:
                st.session_state.visible_hits = 10

            top_hits = hits[:st.session_state.visible_hits]

            for hit in top_hits:
                index = hit['corpus_id']
                row = df.iloc[index]
                st.markdown(f"""
                    **🌐 Site:** {row['url']}  
                    **👤 Username:** `{row['username']}`  
                    **🔑 Password:** `{row['password']}`  
                    ---
                """)

            if st.session_state.visible_hits < len(hits):
                if st.button("Load More"):
                    st.session_state.visible_hits += 10
            else:
                st.info("No more results.")
    except Exception as e:
        st.error(f"Failed to process the file: {e}")
else:
    st.warning("Please upload a CSV file exported from your browser.")
