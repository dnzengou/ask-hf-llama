from dotenv import load_dotenv
import os, streamlit as st

# Load OpenAI API key in env variable
load_dotenv()

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

# Define a simple Streamlit app
st.title("Ask HF Llama")
query = st.text_input("What do you want to know?", "")

# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        try:
            
            #construct_index('https://github.com/dnzengou/yc-startup-playbook/tree/main/ask-yc-paul-graham')
            
            
            #query = input("Enter your query: ")
            template="""Question: {query}
    Answer: Let's think step by step."""            
            prompt = PromptTemplate(template=template, input_variables=["query"])
            llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceHub(repo_id = "google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":64}))
            response = llm_chain.run(query)
            
            #return response

            
            #response = index.query(query)
            st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
