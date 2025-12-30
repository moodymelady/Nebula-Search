
Nebula Search is a local Retrieval-Augmented Generation (RAG) system that allows users to perform semantic searches across their personal PDF documents. The project features a decoupled architecture consisting of a FastAPI backend and a graphical user interface built with CustomTkinter.

System Architecture
The application is divided into two primary components:

Backend Server (app.py): A FastAPI application that manages document indexing and AI processing. It utilizes ChromaDB as a vector store to perform similarity searches and interacts with a local Llama 3.2 model via Ollama to generate context-aware responses.

Frontend UI (search_ui.py): A desktop interface built with CustomTkinter that provides a search bar for user queries. It communicates with the backend via a REST API.

Tech Stack
Language: Python 3.12

AI Engine: Ollama (Llama 3.2)

Frameworks: FastAPI, LangChain

Vector Database: ChromaDB

UI Library: CustomTkinter

Prerequisites
Python 3.12: It is recommended to use the stable 3.12 version to ensure library compatibility.

Ollama: Must be installed and running locally with the Llama 3.2 model downloaded.

Tkinter: Mac users may need to install the graphics bridge via Homebrew using brew install python-tk@3.12.

Installation
Clone the repository and navigate to the project directory:

Bash

cd "resume project"
Create and activate a virtual environment:

Bash

python3.12 -m venv venv
source venv/bin/activate
Install the required dependencies:

Bash

pip install fastapi uvicorn requests langchain-community langchain-ollama chromadb pypdf pydantic-settings customtkinter
Configuration
Create a folder named my_docs in the root directory.

Place the PDF files you wish to index and search into the my_docs folder.

How to Run
Running the application requires two separate terminal tabs to be active simultaneously.

Step 1: Start the Backend
Open a terminal tab, navigate to the project folder, activate the virtual environment, and start the server:

Bash

source venv/bin/activate
python3 app.py

Wait until the terminal displays a message indicating that the application startup is complete.

Step 2: Start the Frontend
Open a second terminal tab, navigate to the project folder, activate the virtual environment, and launch the UI:

Bash

source venv/bin/activate
python3 search_ui.py 

Usage
Enter a query into the search bar of the Nebula Search window.

Press Enter to submit the search.

The system will retrieve relevant information from the indexed PDFs and display a generated answer in the interface.
