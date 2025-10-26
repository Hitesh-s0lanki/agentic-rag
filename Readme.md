# Agentic RAG: Advanced Retrieval-Augmented Generation

A comprehensive collection of advanced RAG (Retrieval-Augmented Generation) implementations and techniques, featuring autonomous agents, multi-modal capabilities, and sophisticated query enhancement strategies.

## 🚀 Overview

This repository contains a modular framework for building sophisticated RAG systems with various advanced techniques including autonomous agents, adaptive retrieval, multi-modal processing, and intelligent query enhancement. Each module is designed to be self-contained and can be used independently or combined for more complex applications.

## 📁 Project Structure

### Core RAG Implementations

- **`rag-implementation/`** - Basic RAG implementations with ReAct agents

  - Basic ARAG (Advanced RAG) patterns
  - ReAct agent integration
  - RAG tool implementations

- **`e2e-project/`** - Complete end-to-end RAG system
  - Full production-ready implementation
  - Streamlit web interface
  - Modular architecture with document processing, vector storage, and graph building

### Advanced RAG Techniques

- **`autonomus-rag/`** - Autonomous RAG with self-reflective capabilities

  - Query planning and decomposition
  - Iterative retrieval strategies
  - Answer synthesis with chain-of-thought reasoning
  - Self-reflection mechanisms

- **`adaptive-rag/`** - Adaptive retrieval strategies

  - Dynamic retrieval parameter adjustment
  - Context-aware retrieval optimization

- **`corrective-rag/`** - Self-correcting RAG systems

  - Error detection and correction
  - Quality assessment and improvement

- **`cache-augmented-rag/`** - Cache-enhanced RAG
  - Intelligent caching strategies
  - Performance optimization through caching

### Multi-Agent Systems

- **`multi-agent-rag/`** - Multi-agent RAG architectures

  - Collaborative agent systems
  - Specialized agent roles

- **`langgraph/`** - LangGraph-based agent implementations
  - State management with Pydantic
  - Multi-tool chatbot systems
  - Streaming capabilities
  - ReAct agent patterns

### Query Enhancement

- **`query-enhancement/`** - Advanced query processing
  - Query decomposition strategies
  - Query expansion techniques
  - HyDE (Hypothetical Document Embeddings)
  - Output optimization

### Data Processing & Storage

- **`data-ingestion/`** - Comprehensive data processing pipeline

  - Multi-format document parsing (PDF, Word, CSV, Excel, JSON, databases)
  - Semantic chunking strategies
  - Document metadata enrichment

- **`vector-embeddings/`** - Vector representation techniques

  - OpenAI embeddings integration
  - Vector representation strategies

- **`vector-store-database/`** - Vector database implementations
  - ChromaDB integration
  - FAISS vector store
  - Pinecone database
  - AstraDB vector database
  - Other vector store options

### Search & Retrieval

- **`hybrid-search-strategies/`** - Advanced search techniques
  - Dense and sparse retrieval combination
  - Maximal Marginal Relevance (MMR)
  - Re-ranking strategies
  - Semantic chunking

### Multi-Modal Capabilities

- **`multi-model-openai/`** - Multi-modal RAG with OpenAI
  - Vision and text processing
  - Multi-modal document understanding

### Experimental Features

- **`graphdb/`** - Graph database experiments
  - Graph-based knowledge representation
  - Prompt strategies for graph databases

## 🛠️ Setup and Installation

### Prerequisites

- Python 3.8+
- OpenAI API key
- UV package manager (recommended) or pip

### Quick Start

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd agentic-rag
   ```

2. **Set up environment:**

   ```bash
   # Using UV (recommended)
   uv init
   uv venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac

   # Or using pip
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

4. **Install dependencies for specific modules:**
   ```bash
   # Navigate to desired module
   cd autonomus-rag
   uv add -r requirements.txt
   # or
   pip install -r requirements.txt
   ```

## 🚀 Getting Started

### Basic Usage

1. **Start with the E2E Project:**

   ```bash
   cd e2e-project
   python main.py
   ```

2. **Run the Streamlit interface:**

   ```bash
   cd e2e-project
   streamlit run streamlit_app.py
   ```

3. **Explore individual modules:**
   - Open Jupyter notebooks in any module's `src/` directory
   - Follow the setup instructions in each module's README

### Example: Autonomous RAG

```python
# Navigate to autonomus-rag module
cd autonomus-rag

# Run the query planning notebook
jupyter notebook src/query_planning_decomposition.ipynb
```

## 📚 Key Features

### 🤖 Autonomous Agents

- Self-reflective query processing
- Iterative retrieval optimization
- Chain-of-thought reasoning
- Multi-step problem solving

### 🔍 Advanced Retrieval

- Hybrid search strategies
- Adaptive retrieval parameters
- Cache-augmented performance
- Multi-modal document processing

### 🧠 Intelligent Query Processing

- Query decomposition and planning
- Hypothetical document embeddings (HyDE)
- Query expansion techniques
- Context-aware retrieval

### 🏗️ Modular Architecture

- Self-contained modules
- Reusable components
- Easy integration and customization
- Production-ready implementations

## 🎯 Use Cases

- **Research and Analysis**: Autonomous research agents for complex queries
- **Document Q&A**: Multi-modal document understanding and question answering
- **Knowledge Management**: Intelligent document retrieval and synthesis
- **Customer Support**: Advanced chatbot systems with retrieval capabilities
- **Content Generation**: Context-aware content creation with source attribution

## 🔧 Configuration

Each module includes its own configuration system. Key configuration areas:

- **API Keys**: OpenAI, vector database credentials
- **Model Settings**: LLM parameters, embedding models
- **Retrieval Parameters**: Chunk sizes, overlap, similarity thresholds
- **Agent Behavior**: Reflection prompts, iteration limits

## 📖 Documentation

Each module contains detailed documentation:

- **README files**: Module-specific setup and usage
- **Jupyter notebooks**: Interactive examples and tutorials
- **Command files**: Quick setup instructions
- **Code comments**: Inline documentation and examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your implementation or improvement
4. Include tests and documentation
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT models and embeddings
- LangChain for the RAG framework
- LangGraph for agent orchestration
- Various vector database providers (ChromaDB, Pinecone, FAISS)

## 📞 Support

For questions, issues, or contributions:

- Open an issue on GitHub
- Check the documentation in each module
- Review the Jupyter notebooks for examples

---

**Note**: This repository is actively maintained and includes cutting-edge RAG techniques. Some modules may require specific API keys or external services. Please refer to individual module documentation for detailed setup instructions.
