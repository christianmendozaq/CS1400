import json

usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# GUARDAR
with open('datos.json', 'w') as f:
    json.dump(usuario, f, indent=4)

"""
open('datos.json', 'w'): abre el archivo datos.json.
'datos.json' es el nombre del archivo.
'w' significa write (escribir). Si el archivo no existe, lo crea; si ya existe, borra su contenido y lo reemplaza.
with ... as f:: es un administrador de contexto. Abre el archivo, lo asigna a la variable f y, al terminar el bloque indentado, lo cierra automáticamente. Por eso no se necesita .close().
f: es el objeto archivo. Es el “puente” entre tu programa y el archivo en el disco.
json.dump(usuario, f, indent=4): convierte el diccionario a JSON y lo escribe en el archivo. Recibe tres cosas:
usuario: lo que se va a guardar.
f: dónde se va a guardar.
indent=4: usa 4 espacios de sangría para que el archivo sea legible.
"""

# LEER
with open('datos.json', 'r') as f:
    datos = json.load(f)
    print(f"Usuario: {datos['nombre']}")

"""
open('datos.json', 'r'): abre el mismo archivo, pero con 'r' (read, leer). Si el archivo no existe, da error FileNotFoundError.
with ... as f:: igual que antes, cierra el archivo automáticamente al terminar.
datos = json.load(f): lee todo el contenido del archivo y lo convierte de nuevo en un diccionario de Python, guardándolo en la variable datos. Es lo opuesto a json.dump(). Ahora true vuelve a ser True.
print(f"Usuario: {datos['nombre']}"):
f"..." es un f-string, que permite insertar variables dentro del texto con llaves {}.
datos['nombre'] accede al valor de la clave "nombre", que es "Estudiante".
Salida en pantalla: Usuario: Estudiante

"""



"""
Preguntas Finales
7. ¿Qué hace la función json.dump()?
    -Convierte un objeto de Python a formato Json y lo escribe en un archivo. En este caso
    guarda el diccionario usuario en datos.json.

8. ¿Cuál es la ventaja de usar with open(...) en lugar de .close()?
    _La ventaja es que el archivo se cierra automaticamente al terminar el bloque de codigo, asi no lo tienes que hacer
    manualmente.
"""