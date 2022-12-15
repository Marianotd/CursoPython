class MiClase:
    variableClase = 'Valor variable clase'

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    @staticmethod
    def metodoEstatico():
        print(MiClase.variableClase)

    @classmethod
    def metodoClase(cls):
        print(cls.variableClase)

    def metodoInstancia(self):
        self.metodoClase()
        self.metodoEstatico()
        print(self.variableClase)
        print(self.variableInstancia)


MiClase.metodoClase()
miObjeto1 = MiClase('Valor variable instancia')
miObjeto1.metodoClase()
miObjeto1.metodoInstancia()
