
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = str(dia)
        self.mes = str(mes)
        self.ano = str(ano)

    def formatada(self):
        dt = self.dia + '/' + self.mes + '/' + self.ano
        print(dt)


d = Data(21, 11, 2007)
d.formatada()