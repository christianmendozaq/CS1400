# ==========================================
#  M5 Tarea 1
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================

# Sección 1: Conteo Inverso con range()
# Analizaremos cómo usar pasos negativos para contar hacia atrás.
# ==========================================

# Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, -1, -2):
    print("Conteo:", i)

"""Análisis:
# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?

Inicio: en el 10 | Fin: en el 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
Por que se parametro determina cuanto se suma en cada iteracion, al ser un numero negativo, le dices que vaya restando esa cantidad.

# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
Por que se excluye el numero del valor final especificado en el range().

Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y 
deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:

Respuesta: for i in range(num, -1, -2):
                print("Conteo:", i)

"""