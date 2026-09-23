
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
print("Evaluación de condiciones para conducir")

# ENTRADA DE DATOS
edad = int(input("Ingresa tu edad: "))

# VERIFICACION 1 DE LA EDAD
if edad < 18:
    print("No puedes conducir por que aun eres menor de edad. Vuelve en un año")
else:
    print("Responde las siguientes preguntas, para completar la solicitud.")

    # PREGUNTAS PARA CONTINUAR
    tiene_licencia = input("¿Tienes licencia vigente? (s/n): ").strip().lower() == "s"
    alcohol = input("¿Has consumido alcohol recientemente? (s/n): ").strip().lower() == "s"
    cansado = input("¿Te sientes cansado o somnoliento? (s/n): ").strip().lower() == "s"

#ESTRUCTURA DE CONTROL PARA EVALUAR CONDICIONES
#CASO 1 ESTA ALCOHOLIZADO O CANSADO
if alcohol or cansado:
    print("No puedes conducir debido a tus condiciones actuales. Entrega las llaves inmediatamente.")
#CASO 2 NO TIENE LICENCIA VIGENTE
elif not tiene_licencia:
    print("No puedes conducir porque no tienes una licencia vigente.")
#CASO 3 TIENE LICENCIA, NO ESTA ALCOHOLIZADO NI CANSADO
elif tiene_licencia and not alcohol and not cansado:
    print("Puedes conducir. Cumples con todos los requisitos! Diosito te bendiga!")

else:
    print("No se puede completar la aplicacion")