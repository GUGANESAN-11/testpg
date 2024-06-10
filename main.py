# import os

# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai


# # Load environment variables
# load_dotenv()

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="Chat with Gemini-Pro!",
#     page_icon=":brain:",  # Favicon emoji
#     layout="centered",  # Page layout option
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Set up Google Gemini-Pro AI model
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')


# # Function to translate roles between Gemini-Pro and Streamlit terminology
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role


# # Initialize chat session in Streamlit if not already present
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])


# # Display the chatbot's title on the page
# st.title("🤖 Gemini Pro - ChatBot")

# # Display the chat history
# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# # Input field for user's message
# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#     # Add user's message to chat and display it
#     st.chat_message("user").markdown(user_prompt)

#     # Send user's message to Gemini-Pro and get the response
#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     # Display Gemini-Pro's response
#     with st.chat_message("assistant"):
#         st.markdown(gemini_response.text)


import os
import streamlit as st
import time
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="SBA INFO SOLUTION",
    page_icon="",  # You can add your icon here
    layout="wide",  # Wide layout similar to your second code snippet
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.markdown('# :white[SBA INFO SOLUTION] ', unsafe_allow_html=True)
st.markdown('## :white[Search Engine] ', unsafe_allow_html=True)

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.empty():
        if message.role == "model":
            st.image('sba_info_solutions_logo.jpg', width=50)
            st.write(message.parts[0].text)
        else:
            st.image('cit_logo_small.png', width=50)
            st.write(message.parts[0].text)

# Input field for user's message
user_prompt = st.text_input("Ask watsonX.AI", key="input_box")
if user_prompt:
    # Add user's message to chat and display it
    st.image('sba_info_solutions_logo.jpg', width=50)
    st.write(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    st.image('sba_info_solutions_logo.jpg', width=50)
    st.write(gemini_response.text)
