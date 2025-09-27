import random as rnd

class Entrenador:
    def __init__(self, nombre, pok):
        self.nombre = nombre
        self.pok = pok

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

class Pokemon:
    def __init__(self, nombre, atq_max = rnd.randint(20,100), vida_max = rnd.randint(150,400)):
        self.nombre = nombre
        self.vida_actual = vida_max

    def stats(self):
        print(f"ATQ: {self.atq_max}  PS: {self.vida_actual}")

def crearEntrenadorPokemon(id):
    if id == 1:
        n1 = input("Inserte su nombre de entrenador: ")
        p1 = input("Ingrese el nombre de su pokemon: ")
        ent1 = Entrenador(n1,p1)
        return ent1
    else:
        n2 = input("Inserte su nombre de un rival: ")
        p2 = input("Ingrese el nombre de su pokemon: ")
        ent2 = Entrenador(n2,p2)
        return ent2

def valorDeAtaque(ar):
    if ar == 1:
        val_atq = rnd.randint(0,pk1.atq_max)
        return val_atq
    else:
        val_atq = rnd.randint(0,pk2.pok.atq_max)
        return val_atq


def defender(n):
    if n == 1:
        v1 = valorDeAtaque(2)
        az = rnd.randint(1,6)
        if az == 6:
            v1 = 0
        nvac = ent.vida_actual - v1
        if nvac < 0:
            nvac = 0

def recuperar():
    pk1.vida_actual = pk1.vida_max

pk1 = Pokemon("Charizard")
RED = Entrenador("Red",pk1)
P = True

while (P == True):
    dec = input("Desea pelear(P) o finalizar(F) la partida?")
    if dec == P:
        pk2 = Pokemon("Reshiram")
        NPC = Entrenador("N",pk2)
        r = str(NPC)
        print("Desafias al entrenador N.")
        print(r)

    p2 = Perro(str(input("Ingrese el nombre de un perro: ")),str(input("Ingrese la edad del perro: ")))
    list_perros.append(p2)
    i = int(input("Ingrese 0 para salir, 1 para mostrar una lista de perros y un numero mayor para quedarse: "))
    if(i <= 0):
        print("///////////////////////////////////////////////////////////////////")
        print("Fin")
        break
    elif (i == 1) :
        print("///////////////////////////////////////////////////////////////////")
        for j in list_perros:
            print(f"Perro: {j.nombre}; Edad: {j.edad}")

    print("///////////////////////////////////////////////////////////////////")

# Acceder a los atributos e invocar un método
print(persona1.nombre)
persona1.saludar()