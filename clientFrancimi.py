import socket
import webbrowser

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))

op = '0'
webbrowser.open('musica.mp3')

while op != '7':
    print("\nOpção 1: Converter de Dólar para Real")
    print("Opção 2: Converter de Euro para Real")
    print("Opção 3: Converter de Bitcoin para Real")
    print("Opção 4: Converter de Horas para Minutos")
    print("Opção 5: Converter de Minutos para Segundos")
    print("Opção 6: Converter de Horas para Segundos")
    print("Opção 7: Encerrar o programa")
    op = input("\nDigite o número da opção: ")
    
    if op == '1':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade em Dólar: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("A quantidade é: R${:.2f}".format(float(data)))

    elif op == '2':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade em Euro: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("A quantidade é: R${:.2f}".format(float(data)))
    
    elif op == '3':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade em Bitcoin: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("A quantidade é: R${:.2f}".format(float(data)))

    elif op == '4':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade de horas: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("O resultado é: ", data, "minutos")

    elif op == '5':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade de minutos: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("O resultado é: ", data, "segundos")

    elif op == '6':
        s.send(op.encode('utf-8'))
        valor = input("\nDigite a quantidade de horas: ")
        s.send(valor.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("O resultado é: ", data, "segundos")
