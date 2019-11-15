from Circulo import Circulo
class Cilindro(Circulo):
    def __init__(self, valorX, valorY, vradio, valtura):
        self.altura = valtura
        Circulo.__init__(self, vradio, valorX, valorY)

    def getAltura(self):
        return self.altura

    def getVolumen(self):
        return Circulo.getArea(self) * self.altura

    def setAltura(self, valtura):
        self.altura = valtura

    def toString(self):
        return "El cilindro tiene como coordenadas: ", Circulo.toString(), " y la altura: ", self.altura