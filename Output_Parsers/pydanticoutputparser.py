from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Setup LLM
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=256, # Increased to ensure full JSON completion
    temperature=0.7,
)
model = ChatHuggingFace(llm=llm)

# 1. REMOVED COMMAS: Trailing commas make these fields tuples, causing errors.
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

# 2. FIXED TYPO: Changed {format_instrcutions} to {format_instructions}
template = PromptTemplate(
    template='Generate name, age and place of a fictional {place} person \n{format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# 3. CHAINING: Recommended 2025 syntax for better reliability
prompt = template.invoke({'place': 'Mysore'})
result = model.invoke(prompt)

# Parse the response content
try:
    final_result = parser.parse(result.content)
    print(final_result)
except Exception as e:
    print(f"Parsing failed. Raw output: {result.content}")
    print(f"Error: {e}")
