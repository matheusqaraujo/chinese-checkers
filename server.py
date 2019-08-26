import socket
from threading import *
import sys

host = sys.argv[1]
port = int(sys.argv[2])
#print('--- Informe os dados do servidor ---')
#host = (input('Host: '))
#port = int(input('Port: '))
#print('------------------------------------\n')

# AF_INET == Protocolo IPV4
# SOCK_STREAM = Comunição TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print('Server criado!')
# Numero de conexoes simultaneas = 5
server.listen(5)
print('Server escutando!\n')
list_of_clients = []

def clientthread(conn, addr):
    jogador = (conn.recv(1024)).decode('utf-8')
    print((jogador + ' (' + str(addr[0]) + ', ' + str(addr[1]) + ') se conectou!'))
    conn.send(bytes('Você se conectou a sala!\n', 'utf-8'))
    while True:
        if jogador != None:
            message = conn.recv(2048)
            message_to_send = message.decode('utf-8')
            broadcast(message_to_send)

def broadcast(message):
    for clients in list_of_clients:
        clients.send(message.encode())

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    Thread(target=clientthread, args=(conn, addr)).start()

conn.close()
server.close()