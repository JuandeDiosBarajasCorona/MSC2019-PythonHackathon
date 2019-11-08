import math

def getArea(radio):
    return math.pi * math.pow(radio,2)

def main():
    ciclo = "S"
    while ciclo == "S" or ciclo == "s":
        radio = float(input("Introduce el radio: "))

        print("La circunferencia es: ",getArea(radio))
        ciclo = input("¿Otro calculo? (S/n)")
    else:
        print("***** Fin del programa *****")

if __name__ == '__main__':
    main()