validos = ["0","1","2","3","4","5","6","7","8","9","-","."]

malopos = False
repite = True
while repite:
    num = input ("Ingrese un numero: ")
    largo = len( num )
    malochar = False
    malog = False
    contg = 0
    contp = 0
    for i in range( largo ):
        if not num[i] in validos:
            malochar = True
        if (num[i]) == "-":
            contg = contg+1
        if (num[i]) == ".":
            contp = contp+1
    malopos = contg == 1 and num[0] != "-"
    malog = contg > 1
    malop = contp > 1
    if malochar or malog or malopos or malop:
        repite = True
        print("La entrada no es valida.")
    else:
        repite = False

numero = float(num)
print( f"numero: {numero} - numero*2 = {numero*2}")