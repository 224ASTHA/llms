from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# This are used for multi-turn messages
chat_template = ChatPromptTemplate([
    # SystemMessage(content='you are a helpful {domain} expert'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')

    # Instead of these we write these because the prev one is not able to replace the placeholders

    ('system','you are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)