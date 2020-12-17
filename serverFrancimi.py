import socket
from conversor import Conversao
from hora import Converter_Hora

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen()

while True:
    conexão, endereço = s.accept()
    print("Server conectado por ", endereço)

    while True:
        data = conexão.recv(1024).decode('utf-8')
        if data == '1':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Conversao(float(valor))
            v1 = con.dolar_real()
            conexão.send(v1.encode('utf-8'))

        elif data == '2':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Conversao(float(valor))
            v1 = con.euro_real()
            conexão.send(v1.encode('utf-8'))

        elif data == '3':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Conversao(float(valor))
            v1 = con.bitcoin_real()
            conexão.send(v1.encode('utf-8'))

        elif data == '4':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Converter_Hora(int(valor))
            v1 = con.hora_minuto()
            conexão.send(v1.encode('utf-8'))

        elif data == '5':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Converter_Hora(int(valor))
            v1 = con.hora_minuto()
            conexão.send(v1.encode('utf-8'))

        elif data == '6':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            con = Converter_Hora(int(valor))
            v1 = con.hora_segundos()
            conexão.send(v1.encode('utf-8'))

        elif data == '7':
            print("Teste de opção", data)
            valor = conexão.recv(1024).decode('utf-8')
            print("Teste de valor", valor)
            conexão.close()
            break