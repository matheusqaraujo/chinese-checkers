import socket
import sys
import select
from threading import *


def client():
    nome = input('Digite o seu nome: ')
    host = (input('Digite o Host: '))
    port = int(input('Digite o Port: '))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    server.send(nome.encode())

    while True:
        # maintains a list of possible input streams
        sockets_list = [sys.stdin, server]
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                if message != None:
                    print(message.decode('utf-8'))
            else:
                message = str(nome + ': ' + input())
                server.send(message.encode())
                sys.stdout.flush()


    server.close()


Thread(target=client).start()
