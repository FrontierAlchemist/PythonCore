from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

# Creating a server socket.
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
# Binding a socket to an address.
tcpServerSocket.bind(ADDR)
# Listening for connedction requests.
tcpServerSocket.listen(5)

while True:
    print('Waiting for connection...')
    # Accepting a client connection requests.
    tcpCliSocket, addr = tcpServerSocket.accept()
    print('... connected from:', addr)
    while True:
        # Get data from client.
        data = tcpCliSocket.recv(BUFSIZE)
        if not data:
            break
        message = f"{ctime()} {str(data, 'utf-8')}"
        tcpCliSocket.send(bytes(message, 'utf-8'))

    tcpCliSocket.close()

tcpServerSocket.close()
