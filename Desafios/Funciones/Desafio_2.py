"""Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
Si ambos números son iguales, debe devolver el nombre de ambas"""

Ciudad_1=input("Ingrese el nombre de la primera ciudad ")
Ciudad_2=input("Ingrese el nombre de la segunda ciudad ")

def relacion(a,b):
    if(a>b):
        print(Ciudad_1)
    elif (a==b):
        print(f"{Ciudad_1} y {Ciudad_2}")
    else:
        print(Ciudad_2)

relacion(int(input("Ingrese la cantidad de toneladas recicladas por la primera ciudad ")),int(input("Ingrese la cantidad de toneladas recicladas por la segunda ciudad ")))