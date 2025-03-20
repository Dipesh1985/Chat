import os 
import google
import google.generativeai as genai
import streamlit as st


genai.configure(api_key="AIzaSyCEdXLoTzLAH0wYpGKMx1vMkenRT94Q1PM")
def chat(text):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(text)
    return response.text


st.header("Welcome to Our Chatbot")
chater=st.chat_input("Enter Any text to search")
if chater:
    text=chat(chater)
    st.write(f"You:      {chater}")
    st.write(f"Bot:       {text}")

