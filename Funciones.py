# Función para imprimir un mensaje
def printMensaje():
    print("Hola, soy una función sin parámetros")

def printMensaje2():
    return "Soy una función que regresa una cadena"

def printMensaje3(cadena):
    print("Mensaje recibido:",cadena)

def main():
    printMensaje()
    print(printMensaje2())
    printMensaje3("Soy una función que recibe parámetros")

if __name__=="__main__":
    main()