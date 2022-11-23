"""150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer.
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse.
Se solicita una función para que dado el ingreso de un elemento, se solicite tipo:
Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse."""

contaminantes = {
    "Bolsa de plastico" : "150 años",
    "Botella pet" : "1000 años",
    "Envase tetrabrik" : "30 años",
    "Chicle" : "5 años"
}

def contamina(a):
    return print(f"El elemento ingresado contamina durante {contaminantes[a.capitalize()]}")

contamina(input("Ingrese el nombre del elemento "))