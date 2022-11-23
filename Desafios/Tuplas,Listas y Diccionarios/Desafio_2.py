"""Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas,
aprendiendo sobre contaminación del agua crea un programa que pida números,
si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero."""

factores_que_afectan_a_los_mares = ("","Las Aguas Residuales","Las Sustancias Químicas Tóxicas",
"Las Aguas Pluviales","El Vertido de Plásticos,","Los Vertidos de Petróleo",
"La Actividad Minera en Alta Mar","El Cambio climático")

cerrar=0

while cerrar==0:
    num = int(input(f"\nIngrese un numero entre 1 y {len(factores_que_afectan_a_los_mares)-1} o digité 0 para cerrar el programa "))
    if(num==0):
        cerrar=1
    elif(num>0 and num<len(factores_que_afectan_a_los_mares)):
        print("\n",factores_que_afectan_a_los_mares[num])
    else:
        print("\nError. El numero ingresado no pertenece a ningun espacio dentro de la tupla")