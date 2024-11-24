from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_community.document_loaders import DataFrameLoader
import pandas as pd
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

load_dotenv()
dataset_dir = os.getenv('dataset_dir')
file_path = os.path.join(dataset_dir, 'HR policies and IT support.txt')

# Read the content of the specified file into a single string
with open(file_path, 'r') as file:
    dataset = file.read()

# Create a DataFrame with a single row containing the text
df = pd.DataFrame([dataset], columns=['text'])

# Print the DataFrame columns to verify
print("DataFrame columns:", df.columns)

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
NVIDIA_KEY = os.getenv('NVIDIA_KEY')
url = os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_KEY")

chat = ChatGroq(temperature=0, model_name="llama3-8b-8192")
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to get help with the documents attached which are given as document context to you.")
]

# Create a DataFrame with a single row containing the concatenated text
df = pd.DataFrame([dataset], columns=['text'])

# Print the DataFrame columns to verify
print("DataFrame columns:", df.columns)

loader = DataFrameLoader(df, page_content_column='text')
documents = loader.load()

# Use the NVIDIA embedding model you've already instantiated
embedding_model = NVIDIAEmbeddings(model_name="nv-embedqa-e5-v5", api_key=NVIDIA_KEY)

# Create Qdrant instance
qdrant = Qdrant.from_documents(
    documents=documents,
    embedding=embedding_model,  # Use the NVIDIA embedding model here
    # ... other parameters if needed ...
)

query = "what is the policy for leave as per document?"
def custom_prompt(query: str):
    results = qdrant.similarity_search(query, k=3)
    source_knowledge = "\n".join([x.page_content for x in results])
    augment_prompt = f"""Using the contexts below, answer the query:

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augment_prompt

prompt = HumanMessage(
    content=custom_prompt(query)
)

messages.append(prompt)
res = chat.invoke(messages)
print(res.content)