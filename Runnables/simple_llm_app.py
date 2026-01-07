from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="mistralai/mistral-small-3.1-24b-instruct:free",
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables = ["topic"],
    template="Suggest a catcy blog title about {topic}"
)

topic = input("Enter a topic : ")

formatted_prompt = prompt.format(topic=topic)

blog_title = llm.invoke(formatted_prompt)

print("Generated blog name", blog_title.content)

# LLMs run karna chahiye tha isme but humlogon ke pass llm free m available nhi tha so hum chatopenai use kiye hai
# use openai models like gpt-3.5-turbo-instruct