
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
edad = int(input("¿Qué edad tienes? "))

if edad <= 17:
    print("Eres menor de edad, aun no puedes conducir.")
elif edad >= 18 and edad <= 70:
    lentes = input("Usas lentes? (s/n): ")
    if lentes.lower() == "s":
        print("¡No puedes conducir sin tus lentes!")
    else:
        print("¡Puedes conducir! Pero recuerda siempre usar tus lentes si los necesitas.")
elif edad > 70:
    audifonos = input("¿Usas audífonos para escuchar? (s/n): ")
    if audifonos.lower() == "s":
        print("¡No olvides tus audífonos al manejar!.")
    else:
        print("¡Puedes conducir! Pero ten cuidado y mantén la atención en la carretera.")
else:
    print("Edad no válida. Por favor ingresa una edad correcta.")     
