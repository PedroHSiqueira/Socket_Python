from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Responda a pergunta abaixo, em português:

aqui é o histórico de mensagens: {context}

Pergunta: {question}

Resposta: 
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ""
    print("Olá! seja bem-vindo, eu me chamo Len, e sou uma IA Chatbot!, escreva 'sair' para encerrar a conversa.")
    while True:
        question = input("Você: ")

        if question.lower() == "sair":
            print("Len: Até mais!")
            break

        result = chain.invoke({"context": context, "question": question})
        print(f"Len: {result}")

        context += f"Você: {question}\nLen: {result}\n"

if __name__ == "__main__":
    handle_conversation()