import os
import hashlib
from typing import List, Union
from pathlib import Path
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

class DocumentProcessor:
    """Handles document loading, caching, and processing"""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50, cache_dir: str = "data"):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    # -------------------- Loaders --------------------
    def load_from_url(self, url: str) -> List[Document]:
        """Load document(s) from a URL"""
        loader = WebBaseLoader(url)
        return loader.load()

    def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
        loader = PyPDFDirectoryLoader(str(directory))
        return loader.load()

    def load_from_txt(self, file_path: Union[str, Path]) -> List[Document]:
        loader = TextLoader(str(file_path), encoding="utf-8")
        return loader.load()

    def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
        loader = PyPDFLoader(str(file_path))
        return loader.load()

    # -------------------- Core Functions --------------------
    def _get_cache_path(self, source: str) -> Path:
        """
        Generate a deterministic filename from URL or file path.
        """
        hash_name = hashlib.md5(source.encode("utf-8")).hexdigest()[:16]
        return self.cache_dir / f"{hash_name}.txt"

    def _save_to_cache(self, cache_path: Path, content: str):
        cache_path.write_text(content, encoding="utf-8")

    def _load_from_cache(self, cache_path: Path) -> Union[str, None]:
        if cache_path.exists():
            return cache_path.read_text(encoding="utf-8")
        return None

    def load_documents(self, sources: List[str]) -> List[Document]:
        """Load from URL, PDF, or TXT with caching"""
        docs: List[Document] = []

        for src in sources:
            cache_path = self._get_cache_path(src)

            # Check cache first
            cached_content = self._load_from_cache(cache_path)
            if cached_content:
                docs.append(Document(page_content=cached_content, metadata={"source": str(src), "cached": True}))
                continue

            # Load new document
            if src.startswith(("http://", "https://")):
                loaded_docs = self.load_from_url(src)
            else:
                path = Path(src)
                if path.is_dir():
                    loaded_docs = self.load_from_pdf_dir(path)
                elif path.suffix.lower() == ".txt":
                    loaded_docs = self.load_from_txt(path)
                elif path.suffix.lower() == ".pdf":
                    loaded_docs = self.load_from_pdf(path)
                else:
                    raise ValueError(f"Unsupported source type: {src}")

            # Combine and cache
            combined_text = "\n\n".join([d.page_content for d in loaded_docs])
            self._save_to_cache(cache_path, combined_text)
            docs.extend(loaded_docs)

        return docs

    def split_documents(self, documents: List[Document]) -> List[Document]:
        return self.splitter.split_documents(documents)

    def process_urls(self, urls: List[str]) -> List[Document]:
        """Load, cache, and split URLs"""
        docs = self.load_documents(urls)
        return self.split_documents(docs)
