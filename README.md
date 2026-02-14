# Intelligent-codebase-rag-assistant
An AI-powered developer assistant that enables natural language querying over a codebase using Retrieval-Augmented Generation (RAG).

This system allows developers to ask questions about a repository and receive accurate, context-aware answers along with source references.

==> Problem Statement

Understanding large codebases is time-consuming. Developers often struggle to:

Locate relevant functions or modules

Understand relationships between components

Onboard quickly to unfamiliar projects

This project solves that by enabling natural language search over code using embeddings + vector search + LLM reasoning.

## System Flow (How It Works)
GitHub Repository
        ↓
ingest.py
        ↓
splitters.py
        ↓
vectorstore.py (HuggingFace Embeddings + ChromaDB)
        ↓
retriever.py (Similarity Search)
        ↓
rag_pipeline.py (Context + LLM)
        ↓
app.py (Streamlit UI → Answer + Sources)

## Tech Stack

Python

Flask (codebase used for testing)

LangChain

HuggingFace Embeddings

ChromaDB (Vector Store)

LLM (for answer generation)

Streamlit (Interactive UI)

## Key Features

🔎 Natural language querying over code

📚 Context-aware responses using RAG

📌 Source file references included in answers

⚡ Fast similarity-based retrieval

🧠 Embeddings-based semantic search

🖥️ Interactive Streamlit interface

## Project Structure
intelligent-codebase-rag-assistant/
│
├── ingest.py          # Code ingestion from GitHub repo
├── splitters.py       # Text chunking logic
├── vectorstore.py     # Embeddings + ChromaDB storage
├── retriever.py       # Similarity search logic
├── llm.py             # LLM configuration & response generation
├── rag_pipeline.py    # RAG orchestration (Retriever + LLM)
├── app.py             # Streamlit UI
└── README.md

## File-wise Explanation (You Can Put This in README)
🔹 ingest.py

Loads and reads source code files from a GitHub repository

Prepares raw code for processing

🔹 splitters.py

Splits large code files into smaller chunks

Ensures optimal token size for embeddings

🔹 vectorstore.py

Generates embeddings using HuggingFace models

Stores embeddings inside ChromaDB

Enables persistent vector storage

🔹 retriever.py

Performs similarity search on stored vectors

Retrieves most relevant code chunks for a query

🔹 llm.py

Configures the Large Language Model

Generates final answer using retrieved context

🔹 rag_pipeline.py

Combines Retriever + LLM

Implements full Retrieval-Augmented Generation workflow

🔹 app.py

Streamlit-based user interface

Accepts natural language queries

Displays answer along with source references

## How to Run the Project

1️⃣ Clone the repository
git clone https://github.com/your-username/intelligent-codebase-rag-assistant.git
cd intelligent-codebase-rag-assistant

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run ingestion
python ingest.py

5️⃣ Launch Streamlit UI
streamlit run app.py

## Example Questions

What is the purpose of blueprints.py?

Does this codebase use FastAPI?

How is JSON serialization handled?

How are HTTP requests simulated in tests?

Which files are critical for request handling?

 ## Impact

Improved developer onboarding speed

Reduced manual code navigation time

Enabled semantic search instead of keyword search

Built a scalable foundation for AI-powered developer tools

## Future Improvements

Add multi-repo support

Implement authentication

Add conversation memory

Optimize chunking strategy

Deploy using Docker / Cloud

👨‍💻 Author

Alagarsamy S
AI/ML Engineer | Data Scientist
Specialized in RAG Systems, LLM Applications, and Intelligent AI Solutions
