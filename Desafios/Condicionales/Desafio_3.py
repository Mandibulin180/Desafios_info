"""Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea
 y no debe existir vegetación del tipo MATORRAL.
 Escribir un programa que determine si es factible la utilización de fertilizantes."""

compuesto = input("Ingrese cuanto porcentaje abarca el compuesto ")
vegetacion= input("Ingrese la vegetacion que se encuentra en la hectaria ").upper()

if(int(compuesto)>10 and vegetacion!="MATORRAL" ):
    print("Es factible la utilización de fertilizantes")
else:
    print("No es factible la utilización de fertilizantes")
