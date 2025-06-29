# app.py
# Main entry point for the RAG Chatbot application.

import os
import sys
import config
import data_handler
import vector_store
import model

def initialize_vector_store():
    """
    Tries to load an existing vector store. If not found, it creates a new one
    from the documents in the documents directory.
    """
    vectorstore = vector_store.load_vector_store()
    
    if vectorstore is None:
        print("No existing index found. Building a new one...")
        
        # Check if the documents directory exists and is not empty
        if not os.path.exists(config.DOCUMENTS_DIR) or not os.listdir(config.DOCUMENTS_DIR):
            print(f"Error: The '{config.DOCUMENTS_DIR}' directory is empty or does not exist.")
            print("Please add your PDF, DOCX, or TXT files to this directory and restart.")
            os.makedirs(config.DOCUMENTS_DIR, exist_ok=True)
            sys.exit(1)
            
        # Load and process documents
        documents = data_handler.load_documents_from_path(config.DOCUMENTS_DIR)
        if not documents:
            print("Error: No documents were successfully loaded. Exiting.")
            sys.exit(1)
            
        doc_chunks = data_handler.split_documents_into_chunks(documents)
        
        # Create and save the vector store
        vectorstore = vector_store.create_and_save_vector_store(doc_chunks)
        if vectorstore is None:
            print("Failed to create the vector store. Exiting.")
            sys.exit(1)
            
    return vectorstore

def main():
    """
    Main function to run the RAG chatbot.
    """
    # Check for API Key
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        print("Please create a .env file and add your GOOGLE_API_KEY.")
        sys.exit(1)

    # Step 1: Initialize the vector store
    vectorstore_instance = initialize_vector_store()
    
    # Step 2: Create the conversational chain
    qa_chain = model.create_conversational_chain(vectorstore_instance)

    # Step 3: Start the conversational loop
    print("\nChatbot is ready! Type 'exit' or 'quit' to end the session.")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        if not query.strip():
            continue

        try:
            # Get the response from the chain
            response = qa_chain.invoke({"query": query})
            answer = response.get("result", "Sorry, I could not find an answer.")
            print(f"\nBot: {answer}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
