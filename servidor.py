import socket
import threading
import chatbot

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Conexão encerrada pelo cliente {addr}")
                break
            mensagem_cliente = data.decode()
            print(f"Cliente {addr}: {mensagem_cliente}")
            if mensagem_cliente.lower() == "sair":
                print(f"Encerrando conexão com {addr}")
                break
            else:
                resposta_servidor = chatbot.chain.invoke({"context": "", "question": mensagem_cliente})
                conn.sendall(resposta_servidor.encode())
                print(f"Servidor: Resposta enviada para {addr}")
    except ConnectionResetError:
        print(f"Conexão com {addr} foi encerrada abruptamente.")
    finally:
        conn.close()
        print(f"Conexão fechada com {addr}")


HOST = ""
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Servidor escutando na porta {PORT}...")

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Clientes ativos: {threading.active_count() - 1}")
