import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class NebulaBrain:
    def __init__(self):
        # setup embedding model with 384 dimensions
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.persist_directory = "chroma_db"
        self.vectordb = None

    def index_documents(self):
        # ensure target directory exists
        if not os.path.exists('./my_docs'):
            os.makedirs('./my_docs')
            
        # load all text files from the directory
        loader = DirectoryLoader('./my_docs', glob="./**/*.txt", loader_cls=TextLoader)
        documents = loader.load()
        
        if not documents:
            print("no documents found in my_docs folder")
            return

        # split documents into smaller chunks for processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)
        
        # create vector store and save to local disk
        self.vectordb = Chroma.from_documents(
            documents=texts, 
            embedding=self.embeddings, 
            persist_directory=self.persist_directory
        )
        print("database indexing complete")

    def search(self, query):
        # load database from disk if not already in memory
        if not self.vectordb:
            self.vectordb = Chroma(
                persist_directory=self.persist_directory, 
                embedding_function=self.embeddings
            )
        
        # perform similarity search
        results = self.vectordb.similarity_search(query, k=3)
        if not results:
            return "no relevant information found in the local documents"
            
        return results[0].page_content
