# ==========================================
# M9 Tarea Peligrosa
#  Christian Mendoza  
#  Fecha: 2026-10-27
# ==========================================
"""
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

9.En la línea except ValueError as e, ¿qué representa la variable e?
    - La variable e representa donde se va a guardar la informacion del error que se capturo dentro del bloque except del ValueError.

10.¿Qué ventaja ofrece la función traceback.format_tb() frente a simplemente mostrar un mensaje amigable al usuario?
    - La ventaja es que nos da a detalle del error, asi hace al usuario mas facil de entender que paso y como corregirlo.
"""
"""
#B. Validación explícita con raise y garantía con finally
#Podemos forzar la creación de nuestras propias excepciones usando raise cuando un dato no cumple con nuestras reglas de negocio,
# y asegurar la ejecución de código final con finally.

print("--- Validación de Rango ---")
num = 0

while num < 1 or num > 10:
    try:
        num = int(input("Ingrese un número del 1 al 10: "))
        
        if num < 1 or num > 10:
            raise Exception("El número está fuera del rango permitido.")
            
    except ValueError:
        print("❌ Error: Formato incorrecto, se esperaba un número.")
    except Exception as e:
        print(f"⚠️ Error de validación: {e}")
    finally:
        print("🔔 [Bloque Finally] Intento de entrada finalizado.")

print(f"¡Número válido ingresado con éxito! ({num})")


11.¿En qué situaciones se ejecutará el código dentro del bloque finally?
    - Se ejecutara siempre, no importa el resultado del try y los except.
12.¿Qué función cumple la palabra clave raise en el condicional if num < 1 or num > 10?
    - Genera un error, en este caso una excepcion si se cumple la condicion.
13.¿Qué ocurre en el bucle while cuando el usuario ingresa un valor válido (ejemplo: 5)?
    - Se termina el bucle whhile y se imprime el finally y el ultimo print.
"""

#Parte 4: Aplicación Práctica — Calculadora Robusta
#Completa el motor de la calculadora interactiva. Debe mantenerse en ejecución continua pidiendo datos hasta que 
# el cálculo se complete correctamente sin ningún error.

def calculadora_segura():
    print("\n--- Calculadora Robusta ---")

    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operador permitido
            if op not in ['+', '-', '*', '/']:
                # TODO 1: Lanza (raise) un ValueError con el mensaje "Operador no válido"
                #pass
                raise ValueError("Operador no válido")

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break  # Salir del bucle si el cálculo se realizó con éxito
            
        # --- MANEJO DE EXCEPCIONES ---

        # TODO 2: Captura el error de formato cuando el usuario ingresa texto en lugar de números
        except ValueError as e:
            if str(e) == "Operador no válido":
                print(f"❌ Error de entrada: {e}")
            else:
                print("❌ Error: Ingrese valores numéricos válidos.")

        # TODO 3: Captura la división por cero
        except ZeroDivisionError as e:
            print(f"❌ Error: No se puede dividir entre cero: {e}")

        # TODO 4: Captura el ValueError (generado por el operador inválido) y muestra e
        #Segun yo se tuvo que modificar en el TODO2 para que pudiera capturar el error y distinguir cual ocurre primero
        #Dure mucho tratando de entender como hacerlo, hasta que entendi que se tenia que hacer un if si usaba el raise y else si usaba
        #el otro ValueError.
        finally:
            # TODO 5: Muestra siempre un mensaje de cierre de intento
           #pass
           print("🔔 [Bloque Finally] Intento de entrada finalizado.") #Lo puse igual que en el ejercicio anterior

calculadora_segura()

"""
14.¿Cuál es el propósito de la instrucción break colocada al final de la sección try?
    -Con el break se finaliza el bucle del while si todo el bucle se realiza de manera correcta.
    Si no se pusiera el break, el programa te seguiria pidiendo numeros aunque la operacion anterior fuera exitosa.

15.Si el usuario ingresa n2 = 0 y op = '/', ¿se llega a ejecutar la línea print(f"✅ Resultado: {resultado}")? 
Explica la secuencia del flujo de ejecución.
    -No, no se ejecuta ese print, por que primero se leen los numeros ingresados, despues el operador, el programa al detectar
    que se quiere dividir entre 0, genera un error de ZeroDivisionError y ahi te lanza el except correspondiente con su print,
    ejecuta el finally y vuelve a correr el while.

16.¿Qué sucedería con la experiencia de usuario si omitimos el bucle while True en este programa?
    -El programa solo se podria utilizar una sola vez, ya sea con error o con un calculo exitoso, por lo tanto si el usuario
    se llegara a equivocar, tendria que volver a correr el programa, haciendolo mas tedioso; en cambio con el while, si te equivocas
    el programa no se detiene y te vuelve a pedir inputs validos.
"""