"""Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..
Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes"""

receta = input("Ingrese el numero de receta ")
lista=[]
con=0

if(int(receta)==1):
    print("Ingredientes comunes : Verduras y Berenjenas")
    print("Ingredientes Receta 1: Lentejas y Apio")
    while con<3:
        ingredientes = input("Ingrese los ingredientes que desea ")
        lista.append(ingredientes.capitalize())
        con+=1
    print(f"La receta elegida es la 1 y los ingredientes son: {lista}")
elif(int(receta)==2):
    print("Ingredientes comunes : Verduras y Berenjenas")
    print("Ingredientes Receta 2: Morron y Cebolla ")
    while con<3:
        ingredientes = input("Ingrese los ingredientes que desea ")
        lista.append(ingredientes.capitalize())
        con+=1
        print(f"La receta elegida es la 2 y los ingredientes son: {lista}")
else:
    print("HIJO DE TU PUTA MADRE ESO NO ES UNA RECETA")
