import math
from Punto import Punto
class Circulo(Punto):
    def __init__(self, vradio, valorX, valorY):
        self.radio = vradio
        Punto.__init__(self, valorX, valorY)

    def getRadio(self):
        return self.radio
    def getArea(self):
        return math.pi * math.pow(self.radio, 2)

    def setRadio(self, valorRadio):
        self.radio = valorRadio

    def toString(self):
        return "La circunferencia tiene como centro: ", str(self.getX()), " , ", str(self.getY()), " y radio igual a: ", str(self.radio)