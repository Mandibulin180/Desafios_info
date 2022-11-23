"""En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar,
de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra.
Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra.
Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento."""

desc_1=0.4
desc_2=0.25
cont=0

while cont<9:
    can_tapitas = int(input("Ingrese la cantidad de tapitas "))
    costo = int(input("Ingrese coste total de los productos "))
    if(can_tapitas>=4):
        costo-=desc_1*costo
        print("Su coste total es de: ",costo," Se le aplico un descuento del 40%")
    elif(can_tapitas==2):
        costo-=desc_2*costo
        print("Su coste total es de: ",costo," Se le aplico un descuento del 25%")
    else:
        print("Su coster total es de: ",costo," No se le aplico ningun descuento")
    cont+=1