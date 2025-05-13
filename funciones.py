# funciones

def fn_suma(a, b):
    #variables locales
    resp = a + b
    return resp
# ^^SCOPE^^
def fn_resta(a, b):
    resp = a - b
    return resp

# programa principal

try:
    num1 = int(input("ingrese un nro: "))
    num2 = int(input("ingrese otro nro: "))

    suma = fn_suma(num1, num2)
    # suma = num1 + num2  #variables globales
    resta = fn_resta(num1, num2)
    multi = num1 * num2
    # para atrapar errores

    divis = num1 / num2
    print(f"La division es: {divis}")
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicacion es: {multi}")
except ValueError:
    print("No es un dato valido")
except ZeroDivisionError:
    print("No se puede dividir por cero")


print("Fin.")