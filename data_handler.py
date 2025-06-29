# data_handler.py
# Handles loading and processing of documents.

import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents_from_path(path):
    """
    Loads all supported documents from a given directory path.
    Supported formats: .pdf, .docx, .txt
    """
    documents = []
    print(f"Loading documents from: {path}")
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
            elif filename.endswith(".docx"):
                loader = Docx2txtLoader(file_path)
            elif filename.endswith(".txt"):
                loader = TextLoader(file_path, encoding='utf-8')
            else:
                print(f"Warning: Skipping unsupported file type: {filename}")
                continue
            
            documents.extend(loader.load())
            print(f"Successfully loaded {filename}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            continue
    return documents

def split_documents_into_chunks(documents):
    """
    Splits a list of documents into smaller chunks for processing.
    """
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    docs_chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(docs_chunks)} chunks.")
    return docs_chunks
