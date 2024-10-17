from modelo.cliente import Cliente

class UI:
    def __init__(self):
        self.clientes = []
        self.productos = []

    # Debemos que colocar bien este metodo
    def buscar_cliente(self):
        dni = input("Ingrese el DNI del cliente: ")
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        
        print(f"No se encontró un cliente con el DNI {dni}.")
        return None

    def mostrar_menu(self):
        print("1. Agregar clientes")
        print("2. Agregar productos")
        print("3. Eliminar clientes")
        print("4. Modificar clientes")
        print("5. Modificar productos")
        print("6. Mostrar cantidad de algún producto")
        print("7. Mostrar lista de clientes")
        print("8. Mostrar la factura de algún cliente")
        print("9. Salir")
        

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        
        nuevo_cliente = Cliente(nombre, direccion, telefono)
        self.clientes.append(nuevo_cliente)
        
        print(f"Cliente {nombre} agregado exitosamente.")

    def agregar_producto(self):
        cliente_encontrado = self.buscar_cliente()

        if cliente_encontrado:
            #metodo para insertar productos
            pass

    def eliminar_cliente(self):
        cliente_encontrado = self.buscar_cliente()

        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)

    def modificar_cliente(self):
        cliente_encontrado = self.buscar_cliente()

        pass

    def modificar_producto(self):
        # Implementar lógica para modificar producto
        pass

    def mostrar_cantidad_producto(self):
        dni = input("Ingrese el DNI del cliente: ")


    def mostrar_lista_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(f"Nombre: {cliente.nombre}, DNI: {cliente.dni}, Factura: {cliente.telefono}")

    def mostrar_factura_cliente(self):
        cliente_encontrado = self.buscar_cliente()
        
        if cliente_encontrado:
            cliente_encontrado.mostrar_facturas()

    def opciones(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.agregar_cliente()
            elif opcion == '2':
                self.agregar_producto()
            elif opcion == '3':
                self.eliminar_cliente()
            elif opcion == '4':
                self.modificar_cliente()
            elif opcion == '5':
                self.modificar_producto()
            elif opcion == '6':
                self.mostrar_cantidad_producto()
            elif opcion == '7':
                self.mostrar_lista_clientes()
            elif opcion == '8':
                self.mostrar_factura_cliente()
            elif opcion == '9':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
