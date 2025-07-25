def registrar_Clientes():
    Viajes = {}
    Cantidad = int(input("¿Cuántos clientes desea registrar? "))
    for a in range(Cantidad):
        Codigo_Cliente = input("Ingrese el Codigo Cliente: ")
        Nombre = input("Ingrese el Nombre Cliente: ")
        destinos = []
        while True:
            cantidades = int(input("¿Cuantos destinos ha visitado (1-5)?: "))
            if 1 <= cantidades <= 5:
                break
            print("Debe ingresar entre 1 a 5 destinos")
        for i in range(cantidades):
            destino = input(f"Ingrese el Destino {i + 1}: ")
            destinos.append(destino)
        Viajes[Codigo_Cliente] = {"Nombre": Nombre, "Destino": destino}
    return Viajes

def Contar_Destinos(Clientes):
    def contar_lista(Lugares_Cliente):
        if not Lugares_Cliente:
            return 0
        return contar_lista(list(Clientes.values()))

while True:
    print("Menu de opciones")
    print("1. Ingreso de Clientes")
    print("2. El listado de clientes con sus destinos")
    print("3. El total de destinos registrados")
    print("4. El cliente con más destinos")
    print("5. Salir")
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                Viajes = registrar_Clientes()
            case 2:
                print("dad")
            case 3:
                print("El total de destinos registrados")
            case 4:
                print("El cliente con mas destinos")
            case 5:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entre 1 y 5.")