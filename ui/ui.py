from modelo.cliente import Cliente
from modelo.factura import Factura

class UI:
    def __init__(self):
        # Si hay tiempo, cambiar la lista de clientes por un diccionario
        self.clientes = []
        self.productos = []

    def buscar_cliente(self):
        dni = input("Ingrese el DNI del cliente: ")
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        
        print(f"No se encontró un cliente con el DNI {dni}.")
        return None

    def mostrar_menu(self):
        # falta arreglar los numeros 
        # (eliminar si se arreglo)
        print("1. Agregar clientes")
        print("2. Agregar productos")
        print("3. Eliminar clientes")
        print("4. Modificar clientes")
        print("5. Modificar productos")
        print("6. Mostrar cantidad de algún producto")
        print("7. Mostrar lista de clientes")
        print("8. Mostrar la factura de algún cliente")
        print("9. Mostrar la factura de algún cliente")
        print("10. Salir")
        

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        dni = input("Ingrese el DNI del cliente: ")
        
        nuevo_cliente = Cliente(nombre, dni)
        self.clientes.append(nuevo_cliente)
        
        print(f"Cliente {nombre} agregado exitosamente.")

    def agregar_producto(self):
        # implementar metodo
        pass

    def eliminar_cliente(self):
        cliente_encontrado = self.buscar_cliente()

        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)

    def modificar_cliente(self):
        cliente_encontrado = self.buscar_cliente()
        if cliente_encontrado:
            nuevo_nombre = input("Ingrese el nombre")
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

    def crear_factura(self):
        cliente_encontrado = self.buscar_cliente()

        if cliente_encontrado:
            nueva_factura = Factura()
            nueva_factura.crear_factura()
            cliente_encontrado.agregar_factura(nueva_factura)
            pass

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
                self.crear_factura()
            elif opcion == '10':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
