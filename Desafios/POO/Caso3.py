"""Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos
imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

class Figura:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo(self):
        if(self.lado1==self.lado2 and self.lado1==self.lado3):
            print("El triangulo es equilatero")
            print(f"Todos los lados son iguales por lo tanto el mas grande es de {self.lado1}")
        elif(self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3):
            print("El triangulo es isosceles")
            if(self.lado1>self.lado2):
                if(self.lado1>self.lado3):
                    print(f"El lado del triangulo mas grande es de {self.lado1}")
                else:
                    print(f"El lado del triangulo mas grande es de {self.lado3}")
            elif(self.lado2>self.lado3):
                print(f"El lado del triengulo mas grande es de {self.lado2}")
            else:
                print(f"El lado del triangulo mas grande es de {self.lado3}")
        else:
            print("El triangulo es escaleno")
            if(self.lado1>self.lado2 and self.lado1>self.lado3):
                print(f"El lado del triangulo mas grande es de {self.lado1}")
            elif(self.lado2>self.lado1 and self.lado2>self.lado3):
                print(f"El lado del triangulo mas grande es de {self.lado2}")
            else:
                print(f"El lado del triangulo mas grande es de {self.lado3}")


triangulo1=Figura(3,8,8)
triangulo2=Figura(6,9,2)
triangulo3=Figura(10,10,10)
triangulo1.tipo()
triangulo2.tipo()
triangulo3.tipo()