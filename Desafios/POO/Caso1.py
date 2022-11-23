class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

fiat = Coche("Rojo",4,200,797)

print(fiat.color)
print(Coche.mro())