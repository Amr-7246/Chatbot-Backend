import os
from dotenv import load_dotenv
import weaviate
from langchain.vectorstores import Weaviate
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

client = weaviate.Client(
    url=os.getenv("WEAVIATE_URL"),
    auth_client_secret=weaviate.AuthApiKey(os.getenv("WEAVIATE_API_KEY")),
    additional_headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")},
)

def get_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = Weaviate.from_documents(docs, embeddings, client=client, by_text=True)
    return vectorstore
