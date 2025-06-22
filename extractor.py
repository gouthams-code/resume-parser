from pathlib import PurePath, Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class Extractor:
    def __init__(self, file: PurePath):
        self.file = file
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 25
        )

    def extract(self):
        match self.file.suffix.lower():
            case ".pdf": return PyPDFLoader(self.file).load_and_split(self.splitter)
            case ".txt": return TextLoader(Path(self.file)).load_and_split(self.splitter)
            case ".doc" | ".docx": return UnstructuredWordDocumentLoader(Path(self.file)).load_and_split(self.splitter)
            case _: raise Exception(415, "Upload a Valid File")