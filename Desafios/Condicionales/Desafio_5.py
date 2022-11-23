"""La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra."""

nombre_B = input("Ingrese en nombre del barrio ")
nombre_B = nombre_B.capitalize()
ubicaccion = input("Ingrese el tipo de barrio (Centrico O No Centrico) ")

if(nombre_B[0]<"M" and ubicaccion == "Centrico" or nombre_B[0]>="M" and ubicaccion=="No Centrico"):
    print("Pertenece a la sección A")
else:
    print("Pertenece a la sección B")
