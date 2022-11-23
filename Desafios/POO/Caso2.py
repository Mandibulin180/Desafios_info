class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindradas):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas
    
    def __str__(self):
        return  f"Color: {self.color}\n"\
                f"Ruedas: {self.ruedas}\n"\
                f"Velocidad: {self.velocidad}\n"\
                f"Cilindrada: {self.cilindradas}\n"\
        
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindradas, carga):
        super().__init__(color, ruedas, velocidad, cilindradas)
        self.carga = carga

    def __str__(self):
        return  f"Color: {self.color}\n"\
                f"Ruedas: {self.ruedas}\n"\
                f"Velocidad: {self.velocidad}\n"\
                f"Cilindrada: {self.cilindradas}\n"\
                f"Carga: {self.carga}\n"

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return   f"Color: {self.color}\n"\
                f"Ruedas: {self.ruedas}\n"\
                f"Tipo: {self.tipo}\n"\

class Motocicleta(Bicicleta,Coche):
    def __init__(self,color,ruedas,tipo,velocidad,cilindradas):
        Bicicleta.__init__(self,color,ruedas,tipo)
        Coche.__init__(self,color,ruedas,velocidad,cilindradas)

    def __str__(self):
        return  f"Color: {self.color}\n"\
                f"Ruedas: {self.ruedas}\n"\
                f"Tipo: {self.tipo}\n"\
                f"Velocidad: {self.velocidad}\n"\
                f"Cilindrada: {self.cilindradas}\n"\

guerrero = Motocicleta("Verde",2,"Urbana",200,310)
chevrolet = Camioneta("Rojo",4,200,500,1000)
honda = Coche("Negro",4,210,200)
bmx = Bicicleta("Azul",2,"Deportiva")
Vehiculos = [guerrero,chevrolet,honda,bmx]

def catalogar(Vehiculos,ruedas=None):
    cont=0
    for i in Vehiculos:
        if(ruedas == i.ruedas):
            print(type(i).__name__)
            print(i)
            cont+=1
        elif(ruedas==None):
                print(type(i).__name__)
                print(i)               
    if(ruedas!=None):
        print(f"Se han encontrado {cont} vehiculos con {ruedas} ruedas")

catalogar(Vehiculos,0)
catalogar(Vehiculos,2)
catalogar(Vehiculos,4)