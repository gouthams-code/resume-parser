from langchain.schema.runnable import Runnable
from langchain.chains.llm import LLMChain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


class TheRag(Runnable):
    def __init__(self, llm, prompt, retriever):
        self.retriver = retriever
        self.llm_chain = LLMChain(llm=llm, prompt=prompt)
        self.document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
        self.retrieval_chain = create_retrieval_chain(
            retriever=self.retriver, combine_docs_chain=self.document_chain
        )

    def invoke(self, input={}, config=None):
        result = self.retrieval_chain.invoke(
            {"input": "Analsye the given resume and parse the result efficiently"}
        )
        return result
``