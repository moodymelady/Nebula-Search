
import os
import uvicorn
from fastapi import FastAPI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM

app = FastAPI()

# 1. Initialize the Models (Make sure Ollama is running!)
llm = OllamaLLM(model="llama3.2")
embeddings = OllamaEmbeddings(model="llama3.2")

# 2. Setup Document Indexing
DOCS_PATH = "./my_docs"
CHROMA_PATH = "./chroma_db"

def get_vectorstore():
    if not os.path.exists(CHROMA_PATH):
        print("Indexing your PDFs for the first time... this may take a minute.")
        all_docs = []
        for file in os.listdir(DOCS_PATH):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(DOCS_PATH, file))
                all_docs.extend(loader.load())
        
        return Chroma.from_documents(
            documents=all_docs, 
            embedding=embeddings, 
            persist_directory=CHROMA_PATH
        )
    else:
        return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

# Initialize the vector store once at startup
vectorstore = get_vectorstore()

@app.get("/search")
async def search(query: str):
    print(f"📩 Searching PDFs for: {query}")
    
    # 3. Find the most relevant pages in your PDFs
    relevant_docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    
    # 4. Ask Llama 3.2 to answer BASED on those pages
    prompt = f"Using ONLY the following context, answer the question.\n\nContext:\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)
    
    return {"answer": response}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
