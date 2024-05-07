from classes.Perro import *
from classes.Gato import *
from classes.Caballo import *
from classes.Hombre import * 

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

        
        