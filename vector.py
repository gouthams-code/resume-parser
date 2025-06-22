from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

class VectorDB(Chroma):
    def __init__(self, chunks):
        super().__init__(embedding_function = SentenceTransformerEmbeddings(model_name = "all-MiniLM-L6-v2"))
        self.add_documents(chunks)

    def retrieve(self, query):
        results = self.as_retriever().get_relevant_documents(query)
        return results
