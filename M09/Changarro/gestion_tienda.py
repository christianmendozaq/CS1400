# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# TODO #3 Agregar comenantarios a cada función explicando qué hace y cómo funciona.

def agregar_producto(inventario, nombre, precio):
    """
    Esta funcion sirve para agregar un producto nuevo, primero trata de convertir el precio a un numero flotante,
    si se reaiza con exito guarda el valor en el diccionario inventario y si se ingresa un valor invalido, se guarda como False.
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False

def buscar_precio(inventario, nombre):
    """
    Busca y devuelve el el precio de un producto del inventario, se pone el None en el .get, por si el producto que ingresaste no existe,
    el programa no "crashie" y te devuelva el valor None.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)

def listar_productos(inventario):
    """
   Primero busca si el diccionario inventario esta vacio, si esta vacio te imprime que esta vacio, y si no esta vacio,
   imprime "Inventario Actual" y corre el for recorriendo el diccionario con el nombre y precio de cada producto con 2 decimales.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")