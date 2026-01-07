from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model =  ChatOpenAI(
   model="openai/gpt-oss-20b:free"
)

template2 = PromptTemplate(
    template = "Greet this person in 5 languages. The name of the person is {name}",
    input_variable=['name']
)

prompt = template2.invoke({'name':'nitish'})

result = model.invoke(prompt)

print(result.content)