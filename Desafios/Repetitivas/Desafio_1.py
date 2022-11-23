"""Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
Modificar el programa anterior para que solamente permita una cantidad fija de intentos."""

usuario="usuario"
contrasenia="contrasenia"
user=""
passw=""
cont=0

while (usuario!=user or contrasenia!=passw) and cont<3:
    user = input("Ingrese el usuario ")
    passw = input("Ingrese la contraseña ")
    cont+=1

if(usuario==user and contrasenia==passw):
    print("\nIngresaste")
else:
    print("\nTe quedaste sin intentos")
