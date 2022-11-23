"""Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas.
Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas."""

print("\n")

participantes=int(input("Ingrese el numero de participantes: "))
cont1=0
cont2=0
cont3=0

for i in range(participantes):
    colillas=int(input("Ingresar cantidad de colillas recolectadas: "))
    if colillas>=200:
        cont3+=1
    elif colillas>=100:
        cont2+=1
    elif colillas<100:
        cont1+=1
print(f"\nEl porcentaje de personas que han conseguido menos de 100 colillas es de: {(cont1*100)/participantes} %")
print(f"El porcentaje de personas que han conseguido menos de 100 colillas es de: {(cont2*100)/participantes} %")
print(f"El porcentaje de personas que han conseguido menos de 100 colillas es de: {(cont3*100)/participantes} %")