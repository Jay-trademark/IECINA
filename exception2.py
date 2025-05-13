"""
Las excepciones son errores que ocurren mientras ejecuta el 
programa. Ejemplo dividir entre cero  o intentar convertir letras en números.

si no las manejamos el programa se detiene. Pero si las capturanmos y controlamos
podemos evitar que el programa termine abruptamente o "se caiga"

raise sirve para lanzar (generar) una exception a propósito, normalmente cuando
detectamos que algo anda malen nuestro "negocio", álculos propios, 
validaciones o lógica.
"""
def fn_validad_edad( edad ):
    if (edad < 18):
        raise ValueError("Debe ser mayor de edad")
    return True

try:
    num1 = int(input("Ingrese una edad: "))
    fn_validad_edad( num1 )
    print( num1 )
except ValueError as error:
    print("Sólo de admiten numeros o ",error)
except Exception:
    print("Oops. algo salió mal")