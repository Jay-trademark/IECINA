# probaremos como validar un int

validos = ["0","1","2","3","4","5","6","7","8","9"]

ok = True
repite = True
while repite:
    num = input("Ingrese un numero: ") #.strip <-- se puede hacer así
    num = num.strip() #Quita espacios por la Izq (lstrip) y la derecha (rstrip) ***NO QUITA ESPACIOS DEL MEDIO***
    print(f"num sin espacios: {num}")
    largo = len ( num ) # determina el largo o numero de caracteres
    print(f"largo: {largo}")
    for i in range( largo ):
        print(f"num[{i}]: {num[i]}")
        if num[i] not in validos:
            ok = False
    if ok:
        repite = False
    else:
        ok = True
if ok:
     print("No son numeros")
else:
    print("Son numeros")

