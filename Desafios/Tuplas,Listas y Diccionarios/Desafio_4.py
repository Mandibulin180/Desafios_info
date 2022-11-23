"""Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.
Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i."""

raza_perros = ("Airedale","Whippet","Beagle","Cavalier","Bedlington",
"English Setter","Fox Hound","Bull Terrier","English Bulldog","Cocker Spaniel")

p = int(input("Ingrese la poscicion en la que inicia "))
n = int(input("Ingrese la cantidades de posiciones que desea recorrer "))

for i in range(p,n+1):
    print(f"\nHola soy un {raza_perros[i]}, cuidame")

