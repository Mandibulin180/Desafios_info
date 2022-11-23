"""Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6"""

ancho = int(input("Ingrese el ancho del tablero "))
alto = int(input("Ingrese el alto del tablero "))

tablero=[]

for i in range(0,int(ancho/2)):
    tablero.extend(["Verde","Blanco"])
print("\n")
for i in range(0,alto):
    print(tablero)