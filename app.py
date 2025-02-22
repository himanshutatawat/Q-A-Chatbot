from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Ollama"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, engine, temperature, max_tokens):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question": question})
    return answer

## Title of the app
st.title('Q&A Chatbot with LLMs')
st.sidebar.title("Settings")


## Drop down to select various OPEN AI models
llm = st.sidebar.selectbox("Select the LLM model",["gemma:2b"])

## Adjust the response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.5)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=100)

## Main interface for user input
st.write("Please enter your question below")
user_input = st.text_area("Question:")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write("Response:")
    st.write(response)
else:
    st.write("Please provide a valid question to get the response")





