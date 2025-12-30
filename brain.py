import os
import sys

# Try to import the tools. If they aren't installed, this will tell us!
try:
    from langchain_ollama import ChatOllama
    from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.document_loaders import DirectoryLoader, TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("✅ All tools loaded successfully!")
except ImportError as e:
    print(f"❌ Error: Missing a tool. Did you run pip install? \nDetails: {e}")
    sys.exit()

# 1. Check for the documents folder
if not os.path.exists('./my_docs'):
    os.makedirs('./my_docs')
    with open('./my_docs/note.txt', 'w') as f:
        f.write("Project Nebula is a secret search tool built on a Mac.")
    print("📁 Created 'my_docs' folder and a test file.")

# 2. THE LIBRARIAN
loader = DirectoryLoader('./my_docs', glob="**/*.txt", loader_cls=TextLoader)
docs = loader.load()

# 3. THE CHOPPER
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 4. THE TRANSLATOR
print("🧠 Turning your notes into math...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 5. THE VAULT
vector_db = Chroma.from_documents(chunks, embeddings)

# 6. THE GENIUS (Asking Ollama)
print("🤖 Talking to Llama 3.2...")
llm = ChatOllama(model="llama3.2")

query = "What is the project code-name?"
relevant_docs = vector_db.similarity_search(query)
context = relevant_docs[0].page_content

prompt = f"Answer this: {query} \nUsing this info: {context}"
response = llm.invoke(prompt)

print("\n--- AI ANSWER ---")
print(response.content)