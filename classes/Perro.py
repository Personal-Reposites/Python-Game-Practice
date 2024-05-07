from classes.comun import Ser_vivo 
#Noted it call the import from the app.py means no from this route

class Perro(Ser_vivo):
    def ladrar(self, objecto):
        return "ladro jau jau " +objecto