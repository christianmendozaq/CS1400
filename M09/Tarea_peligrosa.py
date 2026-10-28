# ==========================================
# M9 Tarea Peligrosa
#  Christian Mendoza  
#  Fecha: 2026-10-27
# ==========================================

#Parte 1: Código Vulnerable a Errores
#Observa y analiza el siguiente segmento de código antes de ejecutarlo:
"""
lst = [1, 3, 7, 3]

# Entrada de datos
num = int(input("Ingrese un número entero: "))

# Operación 1: División
print(10 / num)

# Operación 2: Acceso a Lista
print(lst[num])

# Operación 3: Continuación
print("El programa continuó con éxito.")

Preguntas
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
#Parte 2: Control de Flujo con try / except
#Para evitar que el programa se detenga, envolvemos el código propenso a errores dentro de un bloque try y capturamos las fallas con except.

try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

except ValueError:
    print("❌ Error: Debes ingresar un número entero válido (sin letras).")
except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")
except IndexError:
    print("❌ Error: Indice fuera de rango. Ingresa un numero dentro del rango de la lista.")
except:
    print("❌ Ocurrió un error general.")

print("El programa continúa su ejecución normal...")

"""
Preguntas y Modificaciones
4.Ejecuta el código anterior e ingresa "dos". ¿Qué mensaje se imprime? ¿Se ejecuta la última línea de "El programa continúa..."?
    -❌ Error: Debes ingresar un número entero válido (sin letras).
    El programa continúa su ejecución normal...
    (Si se ejetuta la ultima linea)

5.Ejecuta el código e ingresa 0. ¿Por qué se activa el mensaje "Ocurrió un error general" en lugar del de ValueError?
    -Por que Python lee los except linea por linea, entonces, el primero solo saldria si diera un ValueError, pero como este no es el caso,
    ignora ese except y pasa al siguiente, que es un except generico y por lo tanto se activa ese mensaje de error.

6.Modificación de código 1: Agrega un bloque except ZeroDivisionError específico con el mensaje: "❌ Error: No es posible dividir entre cero."
7.Modificación de código 2: Identifica el tipo de error que ocurre al intentar acceder a un índice inexistente en la lista lst
 (al ingresar 100). Agrega un bloque except específico para capturar dicho error con un mensaje descriptivo.
8.Pega tu código corregido con las 3 excepciones específicas aquí.
try:
    lst = [1, 3, 7, 3]
    num = int(input("Ingrese un número entero: "))
    
    print(10 / num)
    print(lst[num])

except ValueError:
    print("❌ Error: Debes ingresar un número entero válido (sin letras).")
except ZeroDivisionError:
    print("❌ Error: No es posible dividir entre cero.")
except IndexError:
    print("❌ Error: Indice fuera de rango. Ingresa un numero dentro del rango de la lista.")
except:
    print("❌ Ocurrió un error general.")

print("El programa continúa su ejecución normal...")

"""

#PARTE 3 Rastrear Errores con traceback y Controlar raise / finally
# A. Diagnóstico técnico con traceback
#   A veces necesitamos registrar el detalle técnico del error para los desarrolladores sin detener la aplicación.
import traceback

try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError as e:
    print("⚠️ Capturamos un ValueError. Detalle técnico:")
    s = traceback.format_tb(e.__traceback__)
    print(s)

print("El programa continúa...")

"""
9.En la línea except ValueError as e, ¿qué representa la variable e?
    - La variable e representa donde se va a guardar la informacion del error que se capturo dentro del bloque except del ValueError.

10.¿Qué ventaja ofrece la función traceback.format_tb() frente a simplemente mostrar un mensaje amigable al usuario?
    - La ventaja es que nos da a detalle del error, asi hace al usuario mas facil de entender que paso y como corregirlo.
"""