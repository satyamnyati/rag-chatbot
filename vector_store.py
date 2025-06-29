# vector_store.py
# Manages the creation, saving, and loading of the FAISS vector store.

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import config

def get_embeddings_model():
    """Initializes and returns the embedding model."""
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL,
        model_kwargs={'device': 'cpu'} # Use CPU for broad compatibility
    )

def create_and_save_vector_store(docs_chunks):
    """
    Creates a FAISS vector store from document chunks and saves it to disk.
    """
    if not docs_chunks:
        print("Error: No document chunks provided to create the vector store.")
        return None

    print(f"Creating embeddings using '{config.EMBEDDING_MODEL}'...")
    embeddings = get_embeddings_model()

    print("Creating and saving FAISS vector store...")
    try:
        vectorstore = FAISS.from_documents(docs_chunks, embeddings)
        vectorstore.save_local(config.FAISS_INDEX_PATH)
        print(f"Vector store saved successfully at: {config.FAISS_INDEX_PATH}")
        return vectorstore
    except Exception as e:
        print(f"Error creating or saving vector store: {e}")
        return None

def load_vector_store():
    """
    Loads an existing FAISS vector store from disk.
    """
    if not os.path.exists(config.FAISS_INDEX_PATH):
        print("No existing FAISS index found.")
        return None

    print(f"Loading existing FAISS index from {config.FAISS_INDEX_PATH}...")
    try:
        embeddings = get_embeddings_model()
        vectorstore = FAISS.load_local(
            config.FAISS_INDEX_PATH, 
            embeddings,
            # Langchain update requires this parameter for deserialization
            allow_dangerous_deserialization=True 
        )
        print("Index loaded successfully.")
        return vectorstore
    except Exception as e:
        print(f"Error loading index: {e}. Consider rebuilding the index.")
        return None
