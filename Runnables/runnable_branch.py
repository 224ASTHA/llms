from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Summarize the following \n {text}",
    input_variables = ['text']
)

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free"
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)), # tuple hai yeh
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic':'9/11 incident'})
print(result)