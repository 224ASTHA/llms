# For understanding and example propose !!!
# No Longer existed in new version of Langchain


# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     max_new_tokens=128,
#     temperature=0.7,
# )

# model = ChatHuggingFace(llm=llm)

# schema = [
#     # We have provied Response Schema according to the schema we needed to work on
#     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
#     ResponseSchema(name='fact_4', description='Fact 4 about the topic'),
#     ResponseSchema(name='fact_5', description='Fact 5 about the topic')
# ]

# parser = StructuredOutputParser(schema)

# template = PromptTemplate(
#     template = 'Give me 5 facts about {topic} \n {format_instructions}',
#     input_variable=['topic'],
#     partial_variables = {'format_instructions': parser.get_format_instructions()}
# )

# prompt = template.invoke({'topic':'9/11 incident'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result)
# print(result.content)
 