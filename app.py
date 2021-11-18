# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 23:35:07 2021

@author: shuhaili
"""

# Creating GUI with tkinter
from chatgui import clean_up_sentence, bow, predict_class, getResponse, chatbot_response
import streamlit as st


# '''
# # Chatbot
# ## Thank you for contact us and have a good day!
# '''


def get_text():
    input_text = st.text_input("You: ","")
    return input_text
    

st.title("""
NLP Bot  
NLP Bot is an NLP conversational chatterbot. Initialize the bot by clicking the "Send" button. 
""")

st.title("Your bot is ready to talk to you")

        
user_input = get_text()

ind = 1
if st.button('Send'):    
    ind = ind +1

st.text_area("Bot:", value=chatbot_response(user_input), height=200, max_chars=None, key=None)