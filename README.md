Modular RAG Chatbot with Gemini and FAISS

This project provides a fully functional, modular Retrieval-Augmented Generation (RAG) chatbot. It leverages the power of Google's Gemini large language model combined with a local FAISS vector index to answer questions based on a set of documents you provide.

The chatbot can read and process .pdf, .docx, and .txt files, making it a versatile tool for creating a question-answering system for your own knowledge base.
Features

    Modular Design: Code is split into logical modules for better readability and maintenance.

    Multi-Format Document Support: Ingests and processes PDF, DOCX, and plain text files.

    Powerful LLM: Uses Google's gemini-1.5-flash model for high-quality, conversational responses.

    Efficient Retrieval: Employs a FAISS vector store for fast and accurate retrieval of relevant information.

    Persistent Index: Automatically saves the created vector index, so you only process documents once.

    Conversational Interface: Run the chatbot in your terminal for an interactive Q&A session.

Project Structure

.
├── documents/              # Place your source documents here
├── faiss_index/            # Saved FAISS index is stored here
├── .env                    # Your API key is stored here
├── app.py                  # Main entry point for the application
├── config.py               # All configuration constants
├── data_handler.py         # Functions for loading and processing data
├── vector_store.py         # Manages FAISS index creation and loading
├── model.py                # Sets up the LLM and conversational chain
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to be ignored by Git
└── README.md               # This file

Installation

1. Clone the Repository (or use the provided files)

2. Create a Python Virtual Environment

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

Configuration

1. Get Your Google API Key

    Go to Google AI Studio and create an API key.

2. Set Up Your Environment File

    In the project root, create a file named .env and add your key:
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Usage

1. Add Your Documents

Place any .pdf, .docx, or .txt files into the documents directory.

2. Run the Chatbot

Execute the main application script from your terminal.

python app.py

    The first time you run the script, it will process your documents and save a FAISS index to the faiss_index directory. On subsequent runs, it will load the existing index.

3. Interact with the Chatbot

    Once ready, you will see the prompt: You: .

    Type your question and press Enter. To end the session, type exit or quit.