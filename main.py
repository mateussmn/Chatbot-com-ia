#Titulo
#input do chat(campo de mensagem)
#a cada mensagem enviada:
    #mostrar a pergunta e enviar para a ia
    #exibir a resposta ta ia na tela

import streamlit as st

st.write("# Chatbot com IA")

texto_usuario = (st.chat_input("Digite sua pergunta"))

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario ={"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagem"].append(mensagem_usuario)

    resposta_ia = "goiaba"
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)

print(st.session_state["lista_mensagem"])


