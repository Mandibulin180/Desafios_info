"""Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar).
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos."""

continuar = "si"
contactos = {}

while continuar=="si":
    #Agrega claves y valores a un diccionario
    contactos[input("Ingrese su nombre ")] = input("Ingrese el correo electronico ")
    continuar = input("¿Quiere continuar? ")
    continuar.lower()
print(contactos)