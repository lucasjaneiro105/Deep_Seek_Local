from langchain_ollama import ChatOllama
import streamlit as st

modelo = ChatOllama(model="deepseek-r1:1.5b", base_url='<seu-local-host>')
st.set_page_config(page_title="Chat Bot", layout="centered")
st.header('Chat Local com Deepseek 🐋', divider=True)

if "mensagens" not in st.session_state:
    st.session_state['mensagens'] = []
mensagens = st.session_state['mensagens']

for tipo, conteudo in mensagens:
    chat = st.chat_message(tipo)
    chat.markdown(conteudo)

prompt = st.chat_input('Faça uma pergunta 💬')

if prompt:
    mensagens.append(('human', prompt))

    chat = st.chat_message('human')
    chat.markdown(prompt)

    resposta = modelo.invoke(mensagens).content
    mensagens.append(('ai', resposta))

    chat = st.chat_message('ai')
    chat.markdown(resposta)
