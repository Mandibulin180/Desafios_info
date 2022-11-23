"""Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.
Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:
3 letras: Correspondientes a la patente.
Del valor numérico:
Los 3 primeros números corresponden a la patente
El 4 número indica
1- Tiró basura a la vía pública
0 - No tiró basura a la vía pública
El 5 número indica
1- Ya había sido multado el vehículo
0 - Vehículo sin multas.
Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados."""

cont=0
cont1=0
cont3=0
terminar=False

while terminar==False:
    termino = input("¿Desea seguir? Si/No ")
    if(termino=="Si"):
        patentes=input("Ingrese la patente de 5 digitos ")
        cont3+=1 #Contador de vehiculos 
        if(patentes[3]=="1"):
            cont+=1 #Contador de autos que tiraron basura
            if(patentes[4]=="1"):
                cont1+=1 #Contador de autos que tiraron basura y ya habian sido multados
    else:
        terminar=True

print("\nLa cantidad de vehiculos observados es de:",cont3)
print("La cantidad de vehiculos que tiraron basura es de:",cont,", y el porcentaje de estos que ya han sido multados anteriormente es de el:",((cont1*100)/cont),"%")