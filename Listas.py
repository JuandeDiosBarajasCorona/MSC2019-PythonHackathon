lista = []

def insertarItem(item):
    lista.append(item)
    print("Se ha insertado correctamente")

def buscarItem(item):
    x = 0
    ban = 0
    for i in lista:
        if (item == i):
            print("Elemento encontrado en la posición: ",x)
            ban = 1
        x = x + 1
    if ban == 0:
        print("El elemento no existe")

def buscarPosicion(pos):
    x = 0
    for i in lista:
        x = x + 1
    if pos <= x and pos >= (x*-1):
        print(lista[pos])
    else:
        print("Posición no valida")

def modificarItem(item, item2):
    x = 0
    pos = 0;
    for i in lista:
        if (item == i):
            pos = x;
        x = x + 1

    lista.insert(pos,item2)
    lista.remove(item)

def eliminarItem(item):
    lista.remove(item)

def reporte():
    print("Los elementos de la lista son: ")
    for i in lista:
        print(i)

def ejecutar_opcion(opc):
    if opc < 1 or opc > 6:
        print ("Seleccione una opción valida")
        return
    if opc == 1:
        item = input("Ingresa el item a insertar: ")
        insertarItem(item)
    if opc == 2:
        item = input("Ingresa el item a buscar: ")
        buscarItem(item)
    if opc == 3:
        pos = int(input("Ingresa la posición del item que quieres consultar: "))
        buscarPosicion(pos)
    if opc == 4:
        item = input("Ingresa el item a modificar: ")
        item2 = input("Ingresa el nuevo item: ")
        modificarItem(item, item2)
    if opc == 5:
        item = input("Ingresa el item a eliminar: ")
        eliminarItem(item)
    if opc == 6:
        reporte()

def main():
    opc = 1
    while opc != "0":
        print("\n")
        print("***** CRUD con listas *****")
        print("1. Agregar elemento")
        print("2. Buscar elemento")
        print("3. Buscar elemento por posición")
        print("4. Modificar elemento")
        print("5. Eliminar elemento")
        print("6. Desplegar reporte")
        print("0. Salir")
        print("\n")
        opc = int(input("Selecciona una opción: "))
        print("\n")
        ejecutar_opcion(opc)
    else:
        print("***** Fin del programa *****")

if __name__ == '__main__':
    main()

"""
lista2 = [23, False, "Leonardo", 34.12, 'C', lista]

for i in lista2:
    print(i)

lista2.append("Perro")
lista2.append(45)

for i in lista2:
    print(i)

print("Primer elemento de la lista: ",lista2[0])
print("Ultimo elemento de la lista: ",lista2[-1])

"""

