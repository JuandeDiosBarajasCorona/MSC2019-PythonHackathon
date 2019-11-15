class Punto(object):
    # Método constructor
    def __init__(self, valorX, valorY):
        self.x = valorX
        self.y = valorY

    # Lista de métodos get
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    # Lista de metodos set
    def setX(self, valorX):
        self.x = valorX
    def setY(self, valorY):
        self.y = valorY

    # Método toString
    def toString(self):
        return "Las coordenadas del punto son: ", str(self.x) , " , " , str(self.y)