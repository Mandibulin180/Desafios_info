"""Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado
Para ello tendremos 4 opciones:
Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"""

pez=(input("Ingrese el tamaño del pescado "))
pez=pez.lower()
print("\n")

if(pez=="normal"):
    print("Pez en buenas condiciones")
elif(pez=="por debajo de lo normal"):
    print("Pez con problemas de nutrición")
elif(pez=="un poco por encima de lo normal"):
    print("Pez con síntomas de organismo contaminado")
elif(pez=="sobredimencionado"):
    print("Pez contaminado")