"""Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. 
Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena"""

lista_mayor_a_100=[]
lista_menor_que_100=[]

arboles={}

def agregar(arboles):
    continuar = "si"
    while continuar=="si":
        arboles[input("Ingrese nombre de la ciudad ")] = input("Ingrese la cantidad de arboles plantados ")
        continuar = input("¿Quiere continuar? ")
        continuar.lower()

def separar(lista):
    for i in lista:
        if(lista[i]>="100"):
            lista_mayor_a_100.append(i)
        else:
            lista_menor_que_100.append(i)
    for i in lista_mayor_a_100:
        print(f"Las ciuades que superan los 100 arboles plantados son: {i} con {arboles[i]} arboles")
    for i in lista_menor_que_100:
        print(f"Las ciudades que plantaron menos de 100 arboles son: {i} con {arboles[i]} arboles")

agregar(arboles)
separar(arboles)