import streamlit as st
from langchain_community.llms import OpenAI  # Importing the correct module from LangChain

# Setting the title of the Streamlit app
st.title("Simple LLM-App")

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the OpenAI language model
def generate_response(prompt):
    try:
        # Initializing the OpenAI language model with a specified temperature and API key
        llm = OpenAI(api_key=openai_api_key, temperature=0.7)
        # Generating the response using the language model
        response = llm(prompt)
        # Displaying the generated response as an informational message in the Streamlit app
        st.info(response)
    except Exception as e:
        # Handling any exceptions that occur during the API call
        st.error(f"An error occurred: {e}")

# Creating a form in the Streamlit app for user input
with st.form(key='my_form'):
    # Creating a text input widget for the user to input text
    input_text = st.text_area('Enter text here:', '')
    # Creating a submit button to generate a response
    submitted = st.form_submit_button('Submit')
    
    # Checking if the OpenAI API key is valid
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter a valid OpenAI API key starting with 'sk-'")
    
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith("sk-"):
        if input_text.strip() == "":
            st.warning("Please enter some text to generate a response.")
        else:
            generate_response(input_text)
