from CRUD.crudClientes import ClienteCrud

class ControladorCliente:
    def __init__(self, cliente_crud=None):
        self.cliente_crud = ClienteCrud()

    def agregar_cliente(self, nombre, dni):
        try:
            self.cliente_crud.crear_cliente(nombre, dni)
            return True  # Indica que la operación fue exitosa
        except ValueError as e:
            print(e)
            return False  # Indica que ocurrió un error

    def obtener_clientes(self):
        return self.cliente_crud.leer_clientes()

    def buscar_cliente_por_dni(self, dni):
        return self.cliente_crud.buscar_por_cedula(dni)

    def actualizar_cliente(self, dni, nombre):
        try:
            self.cliente_crud.actualizar_cliente(dni, nombre)
            return True
        except ValueError as e:
            print(e)
            return False
        
    def buscar_cliente(self, id, accion):
        try:
            cliente = self.cliente_crud.leer_clientes(id)
            if accion == "Eliminar":
                self.cliente_crud.eliminar_cliente(id)  

            elif accion == "Actualizar":
                self.cliente_crud.actualizar_cliente(id)

            return cliente

        except ValueError as e:
            print(e)
            return None

    def eliminar_cliente(self, dni):
        try:
            self.cliente_crud.eliminar_cliente(dni)
            return True
        except ValueError as e:
            print(e)
            return False