from pathlib import Path
from langchain.llms.ollama import Ollama
from extractor import Extractor
from vector import VectorDB
from prompts import PROMPT
from rag import TheRag
from rich import print

class Parser:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.chunks = Extractor(self.filepath).extract()
        self.vector_db = VectorDB(self.chunks)
        self.llm = Ollama(model = "tinyllama")

    def parse(self):
        retriever = self.vector_db.as_retriever()
        chain = TheRag(llm = self.llm, prompt = PROMPT, retriever = retriever)
        response = chain.invoke()
        return response


file = Path("GOUTHAM S (1).pdf")
parser = Parser(file)
result = parser.parse()
print(result)
