from langchain_community.document_loaders import TextLoader # loded the document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# load the document
loader = TextLoader("docs.txt")
documents = loader.load()

# split the text into smaller chuncks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split(documents)

# Convert the splitted text into embeddings and store it in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create the retriver (fetches the relevant data)
retriever = vectorstore.as_retriever()

# Manually Retrieve relevant Documents
query = "What are the key takeaways from the document?"
retriever_docs = retriever.get_relevant_documents(query)

# Combine Retrived Text into Single Prompt
retriever_text = "\n".join({doc.page_content for doc in retriever_docs})

# Initialize the LLMs
model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    temperature=0.7
)

# Manually pass retriever text to LLM
prompt = f"Based on the following text, answer the question: {query}\n\n{retriever_docs}"
answer = model.invoke(prompt)

# Print the answer
print("Answer : ",answer)