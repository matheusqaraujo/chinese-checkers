import socket
from threading import *

conexoes = []
enderecos = []
jogadores = []

def criarServer():
    print('--- Informe os dados do servidor ---')
    host = (input("Host: "))
    port = int(input("Port: "))
    print('------------------------------------\n')
    # AF_INET == Protocolo IPV4
    # SOCK_STREAM = Comunição TCP
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('Server criado!')
    # Numero de conexoes simultaneas = 5
    s.listen(5)
    print('Server escutando!\n')

def conectar():
    sala = 2
    while sala != 0:
        server, endereco = s.accept()
        conexoes.append(server)
        enderecos.append(endereco)
        msg = 'Conectado a sala!\n'
        server.send(msg.encode())
        jogador = (server.recv(1024))
        print((jogador.decode('utf-8') + ' (' + str(endereco[0]) + ', ' + str(endereco[1]) + ') se conectou!'))
        jogadores.append(jogador)
        sala = sala - 1

def broadcast():
    while True:
        msg = str('Server: ' + input(">> "))
        for i in range(2):
            conexoes[i].send(msg.encode())
            #msg = conexoes[i].recv(1024)
            #print(msg.decode("utf-8"))

#def main():
criarServer()
conectar()
#Thread(target=conectar(), args=().start)
print("cheguei aqui")
#Thread(target=broadcast(), args=().start)
broadcast()


