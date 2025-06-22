from langchain.output_parsers import PydanticOutputParser
from resume_schema import ResumeSchema
from langchain.prompts import ChatPromptTemplate

PROMPT = ChatPromptTemplate.from_template(
    template = """
            Analyze the following resume content and extract the details in the specified format

            {context}

            Retrive the details that are mentioned in the Output Structure

            {format_instrcutions}
        """
).partial(format_instrcutions = PydanticOutputParser(pydantic_object = ResumeSchema).get_format_instructions())
