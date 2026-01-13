# Nebula Search: Triple-Threat AI Architecture

A high-performance, local AI search engine that uses a multi-language microservices architecture to provide real-time document indexing and retrieval.

## 🏗️ The Architecture
This project demonstrates proficiency across the three primary pillars of enterprise software:

* **The Brain (Python/FastAPI):** Handles the Retrieval-Augmented Generation (RAG) logic. It uses **LangChain** and **ChromaDB** to turn unstructured text into mathematical vectors for semantic search.
* **The Face (Java/JavaFX):** A sleek, high-concurrency desktop UI built with **Java 21**. It uses asynchronous HTTP clients to communicate with the backend without freezing the interface.
* **The Guard (C++/FSEvents):** A low-level system monitor that watches the file system. Built with **C++** and Apple's **CoreServices**, it triggers instant re-indexing the moment a file is added or changed.



## 🚀 Technical Achievements
* **Cross-Language Integration:** Implemented an API-first design where Java, Python, and C++ communicate over local network protocols.
* **Vector Embeddings:** Optimized for local performance using the `all-MiniLM-L6-v2` model (384 dimensions) via **HuggingFace**.
* **System-Level Optimization:** Utilized C++ to minimize CPU overhead while monitoring file system changes in real-time.
* **Modern Java Standards:** Built on **Java 21 (LTS)** and **JavaFX 21**, ensuring enterprise-grade stability.

## 🛠️ Setup & Execution
1.  **Activate Environment:** `source venv/bin/activate`
2.  **Start Backend:** `python3 app.py`
3.  **Launch UI:** `./run_ui.sh`
4.  **Start Watchman:** `./watchman`

## 👨‍💻 Why This Matters for Fintech
At a scale like American Express, performance and reliability are non-negotiable. This project showcases my ability to manage complex dependencies, navigate system-level constraints (macOS AArch64/M1), and build modular, decoupled systems that are easy to scale and maintain.
