import openai
import pinecone
import os
import streamlit as st
from llama_index import download_loader
from llama_index import SimpleDirectoryReader
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.storage import StorageContext
from llama_hub.file.unstructured.base import UnstructuredReader
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from llama_index.llms import OpenAI
from datetime import datetime
from llama_index.vector_stores import PineconeVectorStore
from dotenv import load_dotenv

st.title("PeLLM - Private Equity Intelligent Search Engine")
st.write("Built with Llama Index and Pinecone")
st.write("--------------------------------------------------")

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo")

openai.api_key = os.environ.get("OPENAI_API_KEY")
pinecone_api_key =  os.environ.get("PINECONE_API_KEY")
# api_key = ""
environment = "gcp-starter"
index_name = "pellm"

pinecone.init(api_key=pinecone_api_key, environment=environment)

# pinecone.create_index(index_name, dimension=1536, metric="euclidean")
pinecone_index = pinecone.Index(index_name)
# pinecone_index.delete(deleteAll=True)
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)


# file_metadata = lambda x: {"filename": x}
# documents = SimpleDirectoryReader('./data_txt', file_metadata=file_metadata).load_data()

service_context = ServiceContext.from_defaults(chunk_size=1024, llm=llm)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#     documents, service_context=service_context, storage_context=storage_context
# )

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, service_context=service_context
)


query_engine = index.as_query_engine()
# response = query_engine.query("who is the author")
user_query = st.text_input("Enter your query", value="what is the carry fee")
if len(user_query) > 2:
    response = query_engine.query(user_query)
    st.write(response.response)
    st.write("References")
    st.write(response.metadata)
    # st.write(response)
# print(response)
# print(type(response))

