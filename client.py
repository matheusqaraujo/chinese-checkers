import socket

nome = input('Digite o seu nome: ')
host = (input("Digite o Host: "))
port = int(input("Digite o Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(nome.encode())


while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    #msg = str(nome + ': ' + input(">> "))
    #s.send(msg.encode())

#server.close()