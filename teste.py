import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
print("Chave carregada:", os.getenv("OPENAI_API_KEY"))
