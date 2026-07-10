#Titulo
#input do chat(campo de mensagem)
#a cada mensagem enviada:
    #mostrar a pergunta e enviar para a ia
    #exibir a resposta ta ia na tela

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

modelo_ia = OpenAI()

st.write("# Chatbot com IA")

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

texto_usuario = (st.chat_input("Digite sua pergunta"))

for mensagem in st.session_state["lista_mensagem"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario ={"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagem"].append(mensagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagem"], model= "gpt-4o")
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)


