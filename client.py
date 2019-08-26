import socket
from threading import *
import tkinter
import sys

def receive():
    while True:
        msg = client_socket.recv(2048).decode("utf8")
        msg_list.insert(tkinter.END, msg)

def send(event=None):
    msg = my_msg.get() # pega a msg da tela
    my_msg.set("") # limpa o campo de msg
    msg = nome + ": " + msg
    client_socket.send(bytes(msg, "utf8"))

def quit(event=None):
    my_msg.set("<< desistiu >>")
    send()
    client_socket.close() # desconecta do servidor
    top.quit() # fecha a tela do jogo


# Conectando o jogador ao servidor
nome = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])
#nome = input('Digite o seu nome: ')
#host = (input('Digite o Host: '))
#port = int(input('Digite o Port: '))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
client_socket.send(nome.encode())

# Criando a tela principal
top = tkinter.Tk()
top.title("Chinese Checkers: " + nome)

# Janela da conversa
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack() # imprime as msgs
messages_frame.pack() # cria a janela da conversa

# Campo de mandar menssagem
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send) # Enviar a menssagem ao pressionar Enter
entry_field.pack()
send_button = tkinter.Button(top, text="Enviar", command=send) # Envia a menssagem ao pressionar o botão Enviar
send_button.pack()

# Fecha a janela quando clica no X
top.protocol("WM_DELETE_WINDOW", quit)

# Iniciando o jogador e o jogo
Thread(target=receive).start()
tkinter.mainloop()