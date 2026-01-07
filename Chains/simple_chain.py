from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free"
)

template = PromptTemplate(
    template='Generate 5 facts about {topic}',
    input_variable=['topic']
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'topic':'cricket'})
print(result)

chain.get_graph().print_ascii()