from modelo.cliente import Cliente
from modelo.factura import Factura
from CRUD.crud import ClienteCrud, ProductoControlCrud

class UI:
    def __init__(self):
        # Si hay tiempo, cambiar la lista de clientes por un diccionario
        self.clientes = {}
        self.productos = []

    def mostrar_menu(self):

        print("1. Agregar clientes")
        print("2. Agregar productos")
        print("3. Eliminar clientes")
        print("4. Modificar clientes")
        print("5. Modificar productos")
        print("6. Mostrar lista de clientes")
        print("7. Mostrar la factura de algún cliente")
        print("8. Mostrar la factura de algún cliente")
        print("9. Buscar por cedula")
        
        print("10. Salir")
        
    def buscar_por_cedula(self):
        dni = input("Ingrese el DNI del cliente: ")
        cliente = self.cliente_crud.buscar_por_cedula(dni)  
        return cliente

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        dni = input("Ingrese el DNI del cliente: ")
        self.cliente_crud.crear_cliente(nombre, dni)

    def agregar_producto(self):
        registro_ica = input("Ingrese el registro ICA del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación: ")
        valor = float(input("Ingrese el valor del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        self.producto_crud.crear_producto(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)

    def eliminar_cliente(self):
        cliente_encontrado = self.buscar_por_cedula()

        if cliente_encontrado:
            self.cliente_crud.eliminar_cliente(cliente_encontrado.dni)

    def modificar_cliente(self):
        cliente_encontrado = self.buscar_por_cedula()
        if cliente_encontrado:
            nuevo_nombre = input("Ingrese el nombre")
            self.cliente_crud.actualizar_cliente(cliente_encontrado.dni, nuevo_nombre)

    def modificar_producto(self):
        registro_ica = input("Ingrese el registro ICA del producto a modificar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_valor = float(input("Ingrese el nuevo valor del producto: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))
        self.producto_crud.actualizar_producto(registro_ica, nuevo_nombre, nuevo_valor, nueva_cantidad)


    def mostrar_lista_clientes(self):
        clientes = self.cliente_crud.leer_clientes()
        if not clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in clientes:
                print(f"Nombre: {cliente.nombre}, DNI: {cliente.dni}")


    def crear_factura(self):
        cliente_encontrado = self.buscar_por_cedula()

        if cliente_encontrado:
            nueva_factura = Factura()
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
                self.mostrar_lista_clientes()
            elif opcion == '7':
                self.mostrar_factura_cliente()
            elif opcion == '8':
                self.crear_factura()
            elif opcion == '9':
                self.buscar_por_cedula()
            elif opcion == '10':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
