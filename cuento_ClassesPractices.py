class Servivo:
    def __init__(self, name):
        self.name=name

    def correr(self):
        return "corrio"

    def comer(self, objecto):
        return "comio "+ objecto

    def mirar(self, objecto):
        return "miro "+objecto

#---------------------------
class Hombre(Servivo):

    def hablar(self, texto):
        return texto

    def montar(self, objecto):
        return "monto en "+ objecto

    def desmontar(self, objecto):
        return "desmonto de "+ objecto

    def dar(self, objecto):
        return "dio a "+objecto

#---------------------------
class Caballo(Servivo):
    pass
#---------------------------

class Perro(Servivo):
    def ladrar(self, objecto):
        return "ladro jau jau " +objecto

#---------------------------
class Gato(Servivo):
    def maulla(self):
        return "maullo miau miau"

        

#-------|Instancias with NAMES|--------------------

betoben=Perro("El perro")
misuga=Gato("El Gato")
veloz=Caballo("El Caballo")
pedro=Hombre("Pedro Martinez")

comida={
"gato":"tuna",
"hombre":"Arroz",
"perro":"Purrina",
"Caballo":"hierba"
}
#pantalla

print("\n *******************\n")


print(f"""
    {pedro.name} {pedro.montar(veloz.name)}.
    {pedro.name} {pedro.mirar(betoben.name)} y {pedro.desmontar(veloz.name)}.
    {betoben.name}  {betoben.ladrar("a "+misuga.name)} y {misuga.comer(comida["gato"])}.

    {pedro.name} {pedro.dar(betoben.name)} {comida["perro"]}, pero su {veloz.name} {veloz.mirar("a " +pedro.name)},
    y {pedro.name} {pedro.dar(veloz.name)} {comida["Caballo"]},{pedro.name} {pedro.comer(comida["hombre"])} 
    y {misuga.name} {misuga.maulla()} y {misuga.name} {misuga.correr()}

    """)
 
print("*******************\n")

        
        