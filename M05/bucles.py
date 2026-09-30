# ==========================================
#  M5 Tarea 2
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================

"""
# Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
# Analiza el siguiente código para comprender la necesidad de los bucles.
# ==========================================

#Código 1:
# Impresión manual repetitiva
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")

Análisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
Que se tendrian que escribir 100 veces esa linea de codigo, haciendo el programa mas ineficiente y propenso a errores.
Y si quisieras cambiar el mensaje lo tendrias que hacer en las 100 lineas.

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? 
# Explica por qué.
No por que el codigo es estatico (hardcoded) y no permite cambios dinámicos en tiempo de ejecución.

"""

# Sección 2: Bucle while (Iteración Indefinida)
# Analiza cómo la estructura condicional if difiere del bucle while.
# ==========================================

#Código 2:
# Intento de repetición con if
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
    print("Ejecutando el bloque...")
    #respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

"""
Análisis:
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? 
# Explica por qué sucede esto usando un if.
El programa finalizo, por que el if evalua la condicion (si/no) solo una vez aunque se ponga otro input y cambie el valor de la variable respuesta.

Modificación 1A (Cambio a while):
Sustituye la palabra if por la palabra while en el código anterior y ejecútalo de nuevo.

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
El programa sigue repitiendo el bloque mientas la condicion sea verdadera ("si"), a diferencia del if, el while si vuelve a evaluar la condicion
principalmente porque el while permite la repetición indefinida mientras la condición sea verdadera.

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
No, eso depende del usuario, por eso se usa un while cuando no sabes exactamente cuantas veces se cumplirá la condición.

Modificación 1B (Bucle Infinito):
Comenta la línea respuesta = input(...) que está dentro del bloque while. Ejecuta el programa e introduce "si".

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
Entra en un bucle infinito por que la variable "respuesta" siempre sigue siendo "si" y nunca se actualiza dentro del while.

# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
Ctrl + C (en Windows/Linux/macOS) envía una señal de interrupción de teclado (KeyboardInterrupt) a la terminal para forzar la detención
inmediata del script.
"""
