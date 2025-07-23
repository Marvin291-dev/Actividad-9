Viajes = {}

while True:
    print("Menu de opciones")
    print("1. Ingreso de Clientes")
    print("2. El listado de clientes con sus destinos")
    print("3 El total de destinos registrados")
    print("4 El cliente con más destinos")
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                Cantidad = int(input("Ingrese la cantidad de clientes: "))
                for a in range(Cantidad):
                    print(f"\nViajes {a + 1}")
                    Codigo_Cliente = int(input("Ingrese el codigo del cliente: "))
                    Nombre= input("Ingrese el nombre del cliente: ")
                    Destino = {}
