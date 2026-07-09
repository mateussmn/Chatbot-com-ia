#Titulo
#input do chat(campo de mensagem)
#a cada mensagem enviada:
    #mostrar a pergunta e enviar para a ia
    #exibir a resposta ta ia na tela

import streamlit as st

st.write("# Chatbot com IA")

texto_usuario = (st.chat_input("Digite sua pergunta"))

if texto_usuario:
    st.chat_message("user").write(texto_usuario)

    resposta_ia = "goiaba"
    st.chat_message("assistant").write(resposta_ia)


