# ¿Qué hace el bloque try/except ValueError? ¿Qué pasaría si el usuario escribe “veinte” y quitamos ese bloque?
 Convierte la entrada del usuario a numero entero y si el usuario escribe algo que no es numero
 se captura el error y le asiga el valor de 0 para que no se rompa el programa.
 Si el usuario escribe "veinte" el programa se detendria y arrojaria el ValueError, y por lo tanto no se ejecutaria 
 el resto del programa.


**Diccionarios y funciones (los refranes)**
4. ¿Por qué guardamos los refranes en un diccionario y no en una lista? ¿Qué ventaja tiene que el refrán sea la clave y el significado el valor?
Por que el diccionario guarda parejas de clave : valor lo cual hace mas facil "emparejar" y la ventaja de que el refran sea la clave es que se busca el significado sin tener que recorrer tooooda la lista para buscar la coincidencia.

5. ¿Para qué sirven las funciones decir_refran() y decir_refran_especifico()? ¿En qué se diferencian?
La funcion decir_refran() elige un refran con su significado al azar y la funcion decir_refran_especifico() muestra un refran que se le asigna, en este caso dependiendo de la edad.

6. Si quisieras agregar un refrán de tu propia abuela, ¿qué línea tendrías que modificar? ¿Hay que cambiar algo más?
Solo se agrega el refran con su significado dentro del diccionario (ya lo hice en el primer TODO)

**Decisiones (if / elif / else)**
7. En el programa, ¿qué refrán recibe una persona de 18 años? ¿Y una de 17? Explica por qué.
Si eres de 18 años recibes el refran "uno pone y Dios dispone" por que no se cumple el primer if (if edad >= 60:), entonces se pasa el siguiente elif (elif edad >= 18:).
Y si tienes 17 años entra el else por que ninguna de las condiciones anteriores se cumplen, por lo tanto recibes "Haz el bien y no mires a quien."

8. ¿Qué pasaría si cambiáramos el orden y pusiéramos primero if edad >= 18 y después elif edad >= 60? ¿Alguien recibiría alguna vez el refrán de “Agua que no has de beber”?
El refran nunca se mostraria por que cualquier persona igual o mayor de 18 "activaria" el primer if y ya no entraria el siguiente elif.

**API y JSON (Parte 2)**
9. ¿Qué convierte json.loads() y en qué se transforma? ¿Y json.dumps(), qué hace en dirección contraria?
json.loads() convierte una cadena de texto JSON en un diccionario de Python mientras que json.dumps() hace lo contrario y toma el diccionario de Python y lo convieerte en cadena de texto con formato JSON.

10. Para obtener la ciudad del usuario, escribimos datos['address']['city']. ¿Por qué necesitamos dos pares de corchetes?
Por que son datos anidados, con el primer par de corchetes entra a ese diccionario y con el segundo se toma el valor de city.

11. Hay tres tipos de error en esa parte (HTTPError, URLError y JSONDecodeError). ¿Cuál ocurriría si no tienes internet? ¿Y si el servidor responde con una página rota?
Si no tienes internet daria el error URLError por que no se puede establecerce conexion con la direccion web y si el servidor responde con una pagina rota daria el error HTTPError por que el servidor si respondio pero te da un error informatico. (el JSONDecodeError te saldria si responde el servidor pero no es JSON valido.)

12. ¿Por qué es buena idea usar timeout=10 al hacer la petición?
Para que no dure tanto tiempo el programa esperando que responda el servidor y si pasan los 10 segundos se cancela la peticion.

**Juego y reflexión general (Parte 3)**
13. En el juego “Completa el refrán”, ¿cómo divide el programa el refrán en dos mitades? ¿Qué hacen split(), join() y //?
Primero convieete el refran en una lista de palabras, despues calcula la mitad y despues las une con espacios.
split() separa la cadena de texto en una lista de palabras separada por espacios.
join() hace lo contrario que split() une la lista de palabras en un solo texto usando un espacio como separador (o el texto que pongas dentro de las comillas).
// se usa para hacer una division entera, o sea, sin decimales.

14. ¿Para qué sirve el bloque if __name__ == "__main__": al final del archivo?
Sirve para asegurarnos que la funcion principal main() solo se ejecute si lo corremos directamente por si importamos el archivo en otro programa, el codigo main() no se ejecute automaticamente.

15. Pregunta abierta: si tuvieras que agregar una cuarta parte al programa, ¿qué agregarías y qué conceptos nuevos necesitarías usar? 
Me gustaria que el usuario pudiera agregar su propio refran dentro del programa con un input() el concepto nuevo que tendria que dominar/entender bien es el de agregar una clave a un diccionario ya hecho.