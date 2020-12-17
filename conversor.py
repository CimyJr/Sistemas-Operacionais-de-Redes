import requests
import json

requisicao = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacao = json.loads(requisicao.text)
#print(cotacao) #teste para saber quais moedas tem na api

class   Conversao:
    def __init__(self, real):
        self.dolar = float(cotacao['USD']['ask'])
        self.euro = float(cotacao['EUR']['ask'])
        self.bitcoin = float(cotacao['BTC']['ask'])
        self.real = real
    
    
    def dolar_real(self):
        resultado = 0.0
        resultado = self.dolar * float(self.real)
        self.resultadoConversor = str(resultado)
        return self.resultadoConversor 


    def euro_real(self):
        resultado = 0.0
        resultado = self.euro * float(self.real)
        self.resultadoConversor = str(resultado)
        return self.resultadoConversor
    

    def bitcoin_real(self):
        resultado = 0.0
        resultado = self.bitcoin * float(self.real)
        self.resultadoConversor = str(resultado)
        return self.resultadoConversor