from classes.comun import Ser_vivo 
#Noted it call the import from the app.py means no from this route

class Hombre(Ser_vivo):

    def hablar(self, texto):
        return texto

    def montar(self, objecto):
        return "monto en "+ objecto

    def desmontar(self, objecto):
        return "desmonto de "+ objecto

    def dar(self, objecto):
        return "dio a "+objecto