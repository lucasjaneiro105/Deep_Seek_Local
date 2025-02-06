<div align="center">
  <img src="https://github.com/user-attachments/assets/3a0be532-c518-47c8-98bb-510a49c22ee3" alt="image" />
</div>

# Deep_Seek_Local🐋🤖
Sistema de chat simples desenvolvido com Langchain, Ollama e Streamlit, permitindo interação via chat com o usuário. Utiliza o modelo **deepseek-r1:1.5b**, que, mesmo sendo pequeno, demonstra ótimos resultados.

## Visão Geral⚙️
Este projeto é um chatbot local que utiliza tecnologias como Langchain, Ollama e Streamlit para criar uma conversação fluida e eficiente. Ideal para quem busca uma solução simples e funcional para interações via chat.

## Características Principais
- Funciona totalmente offline, sem necessidade de conexão com a internet.
- Interface amigável e fácil de usar, desenvolvida com Streamlit.
- Integração com modelos de linguagem via Ollama.

## Limitações
- O modelo **deepseek-r1:1.5b**, por ser pequeno, pode apresentar respostas mais precisas em inglês do que em outros idiomas.
- A geração de respostas pode ser um pouco lenta, dependendo do hardware utilizado.

## Como Executar
1. **Instale o Ollama**: Baixe e configure o Ollama no seu sistema.
2. **Baixe o modelo**: Utilize o comando `ollama pull deepseek-r1:1.5b` para baixar o modelo de interesse.
3. **Instale as dependências**: Execute `pip install -r requirements.txt` para instalar as bibliotecas necessárias.
4. **Clone o repositório**: Faça o clone do projeto para o seu computador.
5. **Execute o chat**: Rode o comando `streamlit run chat.py` para iniciar o chatbot.
