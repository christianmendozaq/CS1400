# ==========================================
#  M5 Tarea 1
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================
"""
# Sección 1: Conteo Inverso con range()
# Analizaremos cómo usar pasos negativos para contar hacia atrás.
# ==========================================

# Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, -1, -2):
    print("Conteo:", i)

Análisis:
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
# Sección 2: Funciones Matemáticas de Python (math)
# Python incluye funciones matemáticas integradas (built-in) y un módulo especializado llamado math.
# ==========================================

import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A  #Redondea el número decimal -34.5678 a 2 posiciones decimales.
print( round(decNum, 0) )   # Línea B  #Redondea a 0 posiciones decimales, pero al pasar un valor flotante a round(), devuelve un tipo float (por eso conserva el .0).
print( int(decNum) )        # Línea C  #La función int() elimina todos los decimales sin redondear, dejando solo la parte entera.
print( abs(decNum) )        # Línea D  #Devuelve el valor absoluto del número, es decir, elimina el signo negativo haciéndolo positivo.
print( math.pow(intNum, 2) ) # Línea E #Eleva un número a una potencia, En este caso, eleva 9 a la potencia 2. La función math.pow() siempre devuelve un número flotante
print( math.sqrt(intNum) )   # Línea F #Calcula la raíz cuadrada (square root) del número. todas las funciones matemáticas del módulo math convierten internamente el resultado a tipo float.

"""
Predicciones de Salida (Escribe el resultado exacto):
# 5. ¿Resultado de la Línea A round(decNum, 2)? 34.57 

# 6. ¿Resultado de la Línea B round(decNum, 0)? -35.0

# 7. ¿Resultado de la Línea C int(decNum)? -34 (Pista: ¿Redondea o trunca los decimales?) trunca los decimales.

# 8. ¿Resultado de la Línea D abs(decNum)? 34.5678

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)? 81.0

# 10. ¿Resultado de la Línea F math.sqrt(intNum)? 3.0
"""