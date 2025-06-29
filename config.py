# config.py
# Stores all the configuration constants for the application.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- PATHS ---
# Root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory for source documents
DOCUMENTS_DIR = os.path.join(ROOT_DIR, "documents")

# Directory for the FAISS vector store
FAISS_INDEX_PATH = os.path.join(ROOT_DIR, "faiss_index")

# --- MODELS ---
# Embedding model for vectorizing text
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM model for generation
LLM_MODEL = "gemini-1.5-flash"

# --- LLM & CHAIN CONFIG ---
# Temperature for the LLM
LLM_TEMPERATURE = 0.3

# Number of relevant chunks to retrieve
RETRIEVER_K = 3

# --- PROMPT TEMPLATE ---
PROMPT_TEMPLATE = """
You are a helpful assistant who answers questions based on the provided context.
Use the following pieces of context to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
