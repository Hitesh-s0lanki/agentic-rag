# Data Ingestion

![LangChain Document Flow](images/langchain-document.svg)

## Overview

This repository provides a modular framework for ingesting, parsing, and chunking data from various sources (text, CSV, Excel, PDF, Word, JSON, SQL databases) for downstream AI and retrieval-augmented generation (RAG) tasks.

## Folder Structure

- `src/`

  - `core.ipynb`: Core text splitting and document loading examples
  - `csv_excel_parsing.ipynb`: CSV/Excel parsing and metadata enrichment
  - `data_parsing_doc.ipynb`: Word document parsing (docx/txt)
  - `data_parsing_pdf.ipynb`: PDF parsing and chunking
  - `database_parsing.ipynb`: SQL database parsing
  - `json_parsing.ipynb`: JSON/JSONL parsing
  - `data/`: Sample data files for each format

- `images/`
  - `langchain-document.svg`: Document processing flow diagram

## Setup

1. Create and activate a virtual environment:
   ```sh
   uv init
   uv venv
   .venv\Scripts\activate
   uv add -r requirements.txt
   ```
