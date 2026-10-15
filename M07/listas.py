# ==========================================
#  M7 Tarea Listas
#  Christian Mendoza  
#  Fecha: 2026-10-13
# ==========================================

# Manejo de textos y listas
mensaje = "bienvenido al curso de python"
comidas = ["tacos", "torta ahogada", "Mole"]

# Mostrar datos
print(mensaje.upper())
print(comidas[1])

"""
1. Ejecuta el código. ¿Cómo se muestra el texto de la variable mensaje en la consola?
-
bienvenido al curso de python

2. Observa la instrucción print(comidas[0]). ¿Qué comida se imprimió en pantalla y en qué posición de la lista se encuentra?
- tacos, en la posicion 0 de la lista.

*Modificación 1: Métodos de cadenas (Strings)

3. Ejecuta el programa modificado. ¿Qué cambio ocurrió en la salida del texto respecto al código original?
- La salida del texto de la variable "mensaje" se muestra toda en mayusculas.

*Modificación 2: Acceso a elementos de una lista
4. Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
- Tuve que poner el numero 1 por que en las listas se empieza a contar desde el 0.

5. Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.

Observa las opciones y complete las definiciones. Métodos disponibles: insert, append, remove, pop y clear.

6. ¿Qué método elimina todos los elementos de la lista? RESPUESTA: clear

7. ¿Qué método elimina un elemento de la lista por su valor de índice? RESPUESTA: pop

8. ¿Qué método elimina un elemento de la lista usando el valor del elemento? RESPUESTA: remove

9. ¿Qué método agrega un elemento al final de la lista? RESPUESTA: append

10. ¿Qué método agrega un elemento en una ubicación específica? RESPUESTA: insert

"""

#DESAFÍO DE CÓDIGO 1:
playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:
playerNames.remove("Adam")

# 2. Elimine el primer número de la lista (5) usando 'pop':
playerNumbers.pop(0)

# 3. Use 'append' para agregar estas variables a sus listas:
name = "Lucas" 
num = 7
playerNames.append(name)
playerNumbers.append(num)

# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:
playerNames.insert(0, "Raven")
playerNumbers.insert(0, 1)

print("Nombres:", playerNames)
print("Números:", playerNumbers)
#Agregue estos ultimos print para verificar que esuvieran bien los cambios.

