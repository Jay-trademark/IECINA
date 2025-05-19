from version.version import version
from auxiliares.listas import lnombre, lprecio, lstock, fn_actualizar_lista
from auxiliares.validacion_numeros import fn_get_num_valido
from productos.mostrar_producto import fn_mostrar_producto
from productos.buscar_producto import fn_buscar

#Sistema de gestion de inventario para una tienda
#autor: Javiera Inostroza

"""==================[ Programa Principal ]=================="""
try:
    salir = False
    while not salir:
        print(f"=====[ Menú {version} ]=====")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("\nOpcion: ")
    # Opcion 1 "Agregar Producto"
        if (op == "1"):  
            nom = input("Nombre del producto: ")
            lnombre.append( nom )
            precio = fn_get_num_valido("Precio del producto: ")
            lprecio.append( precio )
            canti = fn_get_num_valido("Cantidad del producto: ")
            lstock.append( int(canti))
            print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")
    # Opcion 2 "Listar Producto"
        if (op == "2"):
            largo = len (lnombre)
            for i in range(largo):
                fn_mostrar_producto(lnombre[i], lprecio[i], lstock[i])
    # Opcion 3 "Buscar Por Nombre"
        if (op == "3"):
            nom = input("Nombre del producto a buscar: ")
            pos = fn_buscar(lnombre, nom)
            if pos == -1:
                print(f"El producto {nom} no está en el inventario.")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
    # Opcion 4 "Eliminar Producto"
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
    # Opcion 5 "Modificar Producto"
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
    # Opcion 6 "Salir Del Menú"
        if (op == "6"):
            salir = True
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinación CTRL + C")