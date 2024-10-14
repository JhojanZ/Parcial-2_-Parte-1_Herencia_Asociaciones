from modelo.cliente import Cliente
from modelo.productoControl import ProductoControl
from modelo.factura import Factura

def mostrar_menu():
    print("1. Agregar productos")
    print("2. Agregar clientes")
    print("3. Eliminar clientes")
    print("4. Modificar clientes")
    print("5. Modificar productos")
    print("6. Mostrar cantidad de algún producto")
    print("7. Mostrar lista de clientes")
    print("8. Mostrar la factura de algún cliente")
    print("9. Salir")

def agregar_producto():
    # Implementar lógica para agregar producto
    pass

def agregar_cliente():
    # Implementar lógica para agregar cliente
    pass

def eliminar_cliente():
    # Implementar lógica para eliminar cliente
    pass

def modificar_cliente():
    # Implementar lógica para modificar cliente
    pass

def modificar_producto():
    # Implementar lógica para modificar producto
    pass

def mostrar_cantidad_producto():
    # Implementar lógica para mostrar cantidad de producto
    pass

def mostrar_lista_clientes():
    # Implementar lógica para mostrar lista de clientes
    pass

def mostrar_factura_cliente():
    # Implementar lógica para mostrar factura de cliente
    pass

def opciones():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            agregar_cliente()
        elif opcion == '3':
            eliminar_cliente()
        elif opcion == '4':
            modificar_cliente()
        elif opcion == '5':
            modificar_producto()
        elif opcion == '6':
            mostrar_cantidad_producto()
        elif opcion == '7':
            mostrar_lista_clientes()
        elif opcion == '8':
            mostrar_factura_cliente()
        elif opcion == '9':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
