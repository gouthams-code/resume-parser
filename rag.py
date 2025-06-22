from langchain.schema.runnable import Runnable, RunnableSequence
from langchain.chains.llm import LLMChain
from langchain.schema import Document

class TheRag(Runnable):
    def __init__(self, llm, prompt, retriever):
        self.retriver = retriever
        self.llm_chain = LLMChain(llm = llm, prompt = prompt)

    def invoke(self, input = {}, config = None):
        docs = self.retriver.get_relevant_documents("")
        context_text = "\n\n".join([doc.page_content for doc in docs])
        result = self.llm_chain.run(context = context_text)
        return result