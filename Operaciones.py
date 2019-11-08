def sumar(x,y):
    return x + y

def restar(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    return x / y

def comparar(x,y):
    if (x > y):
        print("El primer número (",x,") es el mayor")
    elif (y > x):
        print("El segundo número (",y,") es mayor")
    else:
        print("Los números son iguales")

def contar(x,y):
    if (x > y):
        for i in range(x,y-1,-1):
            print(i)
    elif (y > x):
        for i in range(x,y+1,1):
            print(i)
    else:
        print("No se puede contar, los números son iguales")


def main():
    ciclo = "S"
    while ciclo == "S" or ciclo =="s":
        x = int(input("Introduce el primer número: "))
        y = int(input("Introduce el segundo número: "))

        print("La suma es: ", str(sumar(x,y)))
        print("La resta es: ", str(restar(x,y)))
        print("La multiplicación es: ", str(multiplicar(x,y)))
        print("La división es: ", str(dividir(x,y)))

        comparar(x,y)
        contar(x,y)

        ciclo = input("¿Otra operación? (S/n)")

if __name__=="__main__":
    main()