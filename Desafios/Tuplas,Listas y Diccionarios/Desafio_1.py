"""Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10.
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. """

cantidad_personas = int(input("Ingrese la cantidad de personas que contestaran el cuestionario "))
lista=[]

for i in range(0,cantidad_personas):
    cont_contaminacion = int(input("Del 1 al 10 cuanto conce sobre contaminación "))
    lista.append(cont_contaminacion)

lista.sort()
print(lista)