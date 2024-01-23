from dotenv import load_dotenv
import streamlit as st 
import os

from PIL import Image
import google.generativeai as genai

#from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI 
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Vectara
from langchain.chains import RetrievalQA


#OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
#VECTARA_CUSTOMER_ID = os.getenv('VECTARA_CUSTOMER_ID')
#VECTARA_CORPUS_ID = os.getenv('VECTARA_CORPUS_ID')
#VECTARA_API_KEY = os.getenv('VECTARA_API_KEY')

load_dotenv()
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit Code
st.title("Invoice App - Welcome")

## Function to load Gemini Pro Vision



