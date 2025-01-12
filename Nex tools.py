import socket
import threading
from colorama import Fore

ascii_art_2 = Fore.MAGENTA + '''
                ███╗   ██╗███████╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                ████╗  ██║██╔════╝╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                ██╔██╗ ██║█████╗   ╚███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗         
                ██║╚██╗██║██╔══╝   ██╔██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
                ██║ ╚████║███████╗██╔╝ ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    [PRIVATE CHAT]
 '''

# Imprime el ASCII art
print(ascii_art_2)

print("Join https://discord.gg/mUvPKDZK")
print("Tool created by $ 3kvodkza")

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'salir':
            print("se ha cerrado la conexión.")
            break
        print(f"Cliente: {message}")
        response = input("Tú ")
        client_socket.send(response.encode())
        if response.lower() == 'salir':
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("Servidor iniciado.")

    client_socket, _ = server_socket.accept()
    print("Conexión establecida.")
    handle_client(client_socket)
    server_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Conectado al servidor.")

    while True:
        message = input("Tú ")
        client_socket.send(message.encode())
        if message.lower() == 'salir':
            break
        response = client_socket.recv(1024).decode()
        if response.lower() == 'salir':
            print("se a cortado conexión.")
            break
        print(f"Servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    role = input("servidor (s) cliente (c)? ")
    if role.lower() == 's':
        start_server()
    else:
        start_client()
