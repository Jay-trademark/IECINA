#Sistema de gestion de inventario para una tienda
#autor: Javiera inostroza

""" version MAJOR.MINOR.PATCH
EJEMPLO V2.4.1

MAJOR: (version mayor): Se incrementa cuando se hacen cambios grandes (Generalmente incompatibles) con la versión anterior.
MINOR: (version menor): Se incrementa cuando se agregan nuevas funcionalidades al sistema pero sin romper la compatibilidad.
PATCH: (parche o revision): Se incrementa cuando se corrigen errores en el sistema o se mejoran funcionalidades
"""

#Historial 
#       15/04/2025 Inicio del desarrollo v1.0.0
#       22/04/2025 Agrega la opcion 5 Modificar Cantidad v1.1.0
#       22/04/2025 Mejora las funciones de 3 y 4 al buscar con while v1.1.1
#       29/04/2025 Cambio de Paradigma, inicio el trabajo con funciones v2.0.0
#       05/05/2025 Se reemplaza el buscar y mostrar producto por funciones y se agrega control de keyboardInterrupt v2.0.1

def fn_get_num_valido(mensaje):
    """
    funcion para validar el ingreso de un valor numerico
    no termina hasta que el valor ingresado es valido
    """
    # dock string
    validos = ["0","1","2","3","4","5","6","7","8","9","-","."]
    malopos = False
    repite = True
    num = 0
    while repite:
        num = input ( mensaje )
        l = len( num )
        malochar = False
        malog = False
        contg = 0
        contp = 0
        for i in range( l ):
            if not num[i] in validos:
                malochar = True
            if num[i] == "-":
                contg = contg+1
            if num[i] == ".":
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
    return(numero)
#fn_get_num_valido


def fn_mostrar_producto(prod, precio, stock):
    """
   \n `Uso:` Muestra un prducto del inventario
   \n `Entrada:` Nombre, precio y cantidad del producto
   \n `Retorna:` Nada
    """
    print("=====================================")
    print(f"Producto: {prod}")
    print("Precio: %5.2f" % precio)
    print(f"Stock: {stock}")
#fn_mostrar_producto


def fn_buscar(lista, nombre):
    esta = False
    i = 0
    l = len (nombre)
    while i < l and not esta:
        if lista[i].upper() == nombre.upper():
            esta = True
        else:
            i = l + 1
    if esta:
        return i
    else:
        return -1
#fn_buscar

"""==================[ Programa Principal ]=================="""
try:
    # listas para administrar los productos
    version = "v2.0.1"
    lnombre = ["Plumon", "Borrador", "Pizarra"]
    lprecio = [1280.0, 3500.0, 13500.0]
    lstock = [20,8,10]

    salir = False
    while not salir:
        print(f"=====[ Menú {version} ]=====")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("Opcion: ")
        #****** Agrega producto 
        if (op == "1"):  
            nom = input("Nombre del producto: ")    
            lnombre.append( nom ) 
            precio = fn_get_num_valido("Precio del producto: ")
            lprecio.append( precio ) 
            canti = fn_get_num_valido("Cantidad del producto: ")
            lstock.append( int(canti))
            print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")
        #****** Listar producto 
        if (op == "2"):  
            largo = len (lnombre)
            for i in range(largo):
                fn_mostrar_producto(lnombre[i], lprecio[i], lstock[i])
        #****** Buscar por Nombre
        if (op == "3"):
            nom = input("Nombre del producto a buscar: ")    
            pos = fn_buscar(lnombre, nom)
            if pos == -1:
                print(f"El producto {nom} no está en el inventario.")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
        #****** Eliminar Producto
        if (op == "4"):
            nom = input("Nombre del producto a Eliminar: ")
            pos = fn_buscar(lnombre, nom)
            if pos != -1:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Seguro que desea eliminar [SI/NO]: ")
                if resp.upper() == "SI":
                    del lnombre[pos]
                    del lprecio[pos]
                    del lstock[pos]
                    print(f"Producto {nom} eliminado.")
                else:
                    print(f"Producto {nom} no se ha eliminado.")
            else:
                print(f"El producto {nom} no está en el inventario.")
    # Opcion 5 "Editando el stock"
        if (op == "5"):
            nom = input("Nombre del producto a modificar: ")
            pos = fn_buscar(lnombre, nom)
            if pos == -1:
                print(f"El producto {nom} no está en el inventario.")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Seguro que desea modificar [SI/NO]: ")
                if resp.upper() == "SI":
                    cant = fn_get_num_valido("Ingrese nueva cantidad: ")
                    lstock[pos] = int(cant)
                    print(f"Stock de {nom} modificado.")
                else:
                    print(f"Producto {nom} no se ha modificado.")
        #****** Salir del menú
        if (op == "6"):
            salir = True
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinación CTRL + C")