#class Ser-vivo

class Ser_vivo:
    def __init__(self, name):
        self.name=name

    def correr(self):
        return "corrio"

    def comer(self, objecto):
        return "comio "+ objecto

    def mirar(self, objecto):
        return "miro "+objecto

#class Hombre
class Hombre(Ser_vivo):

    def hablar(self, texto):
        return texto

    def montar(self, objecto):
        return "monto en "+ objecto

    def desmontar(self, objecto):
        return "desmonto de "+ objecto

    def dar(self, objecto):
        return "dio a "+objecto

#class Caballo
class Caballo(Ser_vivo):
    pass

#class Gato
class Gato(Ser_vivo):
    def maulla(self):
        return "maullo miau miau"

#class Perro

class Perro(Ser_vivo):
    def ladrar(self, objecto):
        return "ladro jau jau " +objecto




