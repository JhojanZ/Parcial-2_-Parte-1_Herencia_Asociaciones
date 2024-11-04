from modelo.cliente import Cliente
from modelo.factura import Factura
from CRUD.crud import ClienteCrud, ProductoControlCrud

class UI:
    def __init__(self):
        self.clientes_crud = ClienteCrud()
        self.productos_crud = ProductoControlCrud()

    def mostrar_menu(self):

        print("1. Agregar clientes")
        print("2. Agregar productos")
        print("3. Crear factura")
        print("4. Eliminar clientes")
        print("5. Modificar clientes")
        print("6. Modificar productos")
        print("7. Mostrar lista de clientes")
        print("8. Mostrar la factura de algún cliente")
        print("9. Buscar por cedula")
        
        print("10. Salir")
        
    def buscar_por_cedula(self):
        dni = int(input("Ingrese el DNI del cliente: "))
        cliente = self.clientes_crud.buscar_por_cedula(dni)  
        if cliente:
            return cliente
        else:
            print(f"No se encontró un cliente con cédula: {dni}")
            return None

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        dni = int(input("Ingrese el DNI del cliente: "))
        self.clientes_crud.crear_cliente(dni=dni, nombre=nombre)

    def agregar_producto(self):
        registro_ica = input("Ingrese el registro ICA del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación: ")
        valor = float(input("Ingrese el valor del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        self.productos_crud.crear_producto(registro_ica, nombre_producto, frecuencia_aplicacion, valor, cantidad)

    def pedir_factura(self):
        fecha = input("Ingrese la fecha: ")
        valor = input("Ingrese el valor de la compra: ")

        cantidad_productos = int(input("Ingrese la cantidad de productos: "))
        print("Ingrese los productos")
        productos = []
        for i in range(cantidad_productos):
            producto = input()
            productos.append(producto)

        cantidad_antibioticos = int(input("Ingrese la cantidad de antibioticos: "))
        print("Ingrese los productos")
        antibioticos = []
        for i in range(cantidad_antibioticos):
            antibiotico = input()
            antibioticos.append(antibiotico)

        return Factura(fecha, valor, productos, antibioticos)

    def crear_factura(self):
        cliente_encontrado = self.buscar_por_cedula()

        if cliente_encontrado:
            nueva_factura = self.pedir_factura()
            cliente_encontrado.agregar_factura(nueva_factura)
            pass

    def eliminar_cliente(self):
        cliente_encontrado = self.buscar_por_cedula()

        if cliente_encontrado:
            self.clientes_crud.eliminar_cliente(cliente_encontrado.dni)

    def modificar_cliente(self):
        cliente_encontrado = self.buscar_por_cedula()
        if cliente_encontrado:
            nuevo_nombre = input("Ingrese el nombre")
            self.clientes_crud.actualizar_cliente(cliente_encontrado.dni, nuevo_nombre)

    def modificar_producto(self):
        registro_ica = input("Ingrese el registro ICA del producto a modificar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_valor = float(input("Ingrese el nuevo valor del producto: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))
        self.productos_crud.actualizar_producto(registro_ica, nuevo_nombre, nuevo_valor, nueva_cantidad)

    def mostrar_factura_cliente(self):
        cliente = self.buscar_por_cedula()

        if cliente:
            cliente.mostrar_facturas() 
        else:
            print("Cliente no encontrado.")


    def mostrar_lista_clientes(self):
        clientes = self.clientes_crud.leer_clientes()

        if not clientes:
            print("No hay clientes registrados.")
            return None
        
        for cliente in clientes:
            print(f"Nombre: {cliente.nombre}, DNI: {cliente.dni}")

    def opciones(self):
        while True:
            self.mostrar_menu()
            print("--------------------------------")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.agregar_cliente()
            elif opcion == '2':
                self.agregar_producto()
            elif opcion == '3':
                self.crear_factura()
            elif opcion == '4':
                self.eliminar_cliente()
            elif opcion == '5':
                self.modificar_cliente()
            elif opcion == '6':
                self.modificar_producto()
            elif opcion == '7':
                self.mostrar_lista_clientes()
            elif opcion == '8':
                self.mostrar_factura_cliente()
            elif opcion == '9':
                self.buscar_por_cedula()
            elif opcion == '10':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    interfaz = UI() 
    interfaz.opciones()