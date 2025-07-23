Viajes = {}

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
                Cantidad = int(input("Ingrese la cantidad de clientes: "))
                for a in range(Cantidad):
                    print(f"\nViajes {a + 1}")
                    Codigo_Cliente = int(input("Ingrese el codigo del cliente: "))
                    Nombre = input("Ingrese el nombre del cliente: ")
                    print("Listado de lugares turisticos")
                    Destinos = {}
                    LugaresTuristicos = int(input("Ingrese la cantidad de lugares turisticos que desea: "))
                    for b in range(LugaresTuristicos):
                       lugar = input("Nombre del lugar que visita: ")
                       print(f"\Destinos {lugar} se guardo correctamente")
                       Viajes [Codigo_Cliente] = {
                            "nombre": Nombre,
                            "destinos": Destinos,
                            "codigo": Codigo_Cliente
                        }
            case 2:


              def mostrar_listado(clientes):
                    print("\n📋 Listado de Clientes con sus Destinos:")
                    for codigo, datos in clientes.items():
                        print(f"\nCódigo del cliente: {codigo}")
                        print(f"Nombre: {datos['nombre']}")
                        print("Destinos:")
                        for destino in datos['destinos']:
                         print(f" - {destino}")

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