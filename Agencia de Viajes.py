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
                if not Viajes:
                    print("El cliente no se encontro")
                else:
                    for Codigo_Cliente, Datos in Viajes.items():
                        print(f"\nCodigo del cliente: Codigo")
                        print(f"Nombre: {Datos['Nombre']}")
                        print(f"Destinos: ")
                        for Destino, Datos in Datos['Destinos'].items():
                            print(f" {Datos}:")
                            print(f" Tarea {Datos['Nombre']}")
                            print(f" Parcial {Datos['Destino']}")
                            print(f" Proyecto {Datos['Codigo']}")

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