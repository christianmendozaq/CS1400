# ==========================================
# M9 Tarea Peligrosa
#  Christian Mendoza  
#  Fecha: 2026-10-27
# ==========================================

#Parte 1: Código Vulnerable a Errores
#Observa y analiza el siguiente segmento de código antes de ejecutarlo:

lst = [1, 3, 7, 3]

# Entrada de datos
num = int(input("Ingrese un número entero: "))

# Operación 1: División
print(10 / num)

# Operación 2: Acceso a Lista
print(lst[num])

# Operación 3: Continuación
print("El programa continuó con éxito.")

"""Preguntas
1. Analiza las operaciones antes de ejecutar:
¿Por qué la Operación 1 (10 / num) fallará si el usuario ingresa 0?
    -Por que Python no puede dividir entre 0, por lo tanto dara un error.

¿Por qué la Operación 2 (lst[num]) fallará si el usuario ingresa 100?
    -Por que en la lista solo hay 4 elementos (del 0 al 3), por lo tanto no puede acceder al indice 100, por que no existe.

2. Ejecución y pruebas: Ejecuta el programa tres veces con las entradas indicadas y completa la siguiente tabla de resultados:
Entrada del usuario	¿Llegó a imprimirse "El programa continuó..."? (Sí/No)	Nombre exacto de la excepción generada en consola

"dos"	-No se immrime la operacion 3 y da el error: ValueError: invalid literal for int() with base 10: 'dos'
0	    -No se immrime la operacion 3 y da el error: ZeroDivisionError: division by zero
100	    -No se immrime la operacion 3 y da el error: IndexError: list index out of range    

3. ¿Qué ocurre con la ejecución de las líneas de código subsiguientes cuando Python encuentra un error no capturado en una línea previa?
- Se detiene el programa y te da un mensaje de error en la consola, por lo tanto las siguientes lineas de codigo no se ejecutan.
"""
