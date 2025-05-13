"""
Las excepciones son errores que ocurren mientras se ejecuta el programa.
Ejemplo: dividir por cero o intentar cpnvertir letras en numeros.

Si no las manejamos el programa se detiene.
Pero si las capturamos y controlamos podemos evitar que el programa termine 
abruptamente o "se caiga".
"""
def fn_validar_edad( edad ):
    if (edad < 18 ):
        raise ValueError("debe ser mayor de edad.")
    #El codigo se corta y se termina de ejecutar/leer en el momento en que se levanta un error.
    return True

try:
    num1 = int(input("Ingrese una edad: "))
    fn_validar_edad( num1 )
    print( num1 )
except ZeroDivisionError:
    print("El divisor no puede ser cero.")
except ValueError as error:
    print("Solo se admiten numeros o", error)
except Exception:
    print("Oops. Algo salio mal.")
