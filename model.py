# model.py
# Handles the setup of the LLM and the conversational chain.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import config

def create_conversational_chain(vectorstore):
    """
    Creates the RetrievalQA chain with a custom prompt for the LLM.
    """
    print("Setting up the conversational chain...")
    
    # Initialize the LLM (Gemini 1.5 Flash)
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL,
        temperature=config.LLM_TEMPERATURE
    )

    # Define the prompt template
    prompt = PromptTemplate(
        template=config.PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    # Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={'k': config.RETRIEVER_K}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    print("Conversational chain created successfully.")
    return qa_chain
