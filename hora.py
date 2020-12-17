class Converter_Hora:
    def __init__(self, valor):
        self.valor = valor


    def hora_minuto(self):
        resultado = 0
        resultado = 60 * int(self.valor)
        self.resultadoConversor = str(resultado)
        return self.resultadoConversor
        
        
    def hora_segundos(self):
        resultado = 0
        resultado = 3600 * int(self.valor)
        self.resultadoConversor = str(resultado)
        return self.resultadoConversor
            

