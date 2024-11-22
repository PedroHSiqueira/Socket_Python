import socket
import os

template_menu = """
===================================================================
Seja bem-vindo ao Chatbot, escreva 'sair' para encerrar a conversa.
===================================================================
Escolha uma opção:

1 - Iniciar conversa
2 - Encerrar conexão
"""

template_resposta = """
===================================================================
Resposta do servidor
===================================================================
"""

HOST = "localhost"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((HOST, PORT))
    print("Conectado ao servidor.")
except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor.")
    exit()

try:
    while True:
        os.system("cls")
        print(template_menu)
        mensagem = input("Você (cliente): ")
        if mensagem.lower() == "sair":
            print("Encerrando conexão.")
            break
        cliente.sendall(mensagem.encode())
        data = cliente.recv(1024)
        if not data:
            print("Conexão encerrada pelo servidor.")
            break
        resposta_servidor = data.decode()
        print(template_resposta)
        print(f"{resposta_servidor}")
        input("\nPressione Enter para continuar...")
except KeyboardInterrupt:
    print("\nConexão interrompida pelo usuário.")
finally:
    cliente.close()
    print("Conexão fechada.")
