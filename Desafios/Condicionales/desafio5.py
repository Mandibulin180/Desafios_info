"""La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra."""

nombre_B = input("Ingrese en nombre del barrio ")
nombre_B = nombre_B.capitalize()
ubicaccion = input("Ingrese el tipo de barrio (Centrico O No Centrico) ")
anteriores_M = ["A","B","C","D","E","F","G","H","I","J","K","L"]
posteriores_M = ["M","N","O","P","Q","R","S","T","U","V","W","Y","Z"]

def menorqueM(a,b):
    bande=False
    for i in a:
        if(i==b[0]):
            bande=True
    return bande      

if(ubicaccion=="Centrico" and menorqueM(anteriores_M,nombre_B)):
    print("Pertenece a la seccion A")
elif(ubicaccion=="No Centrico" and menorqueM(posteriores_M,nombre_B)):
    print("Pertenece a la seccion A")
else:
    print("Pertenece a la sección B")