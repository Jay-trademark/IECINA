def fn_mostrar_producto(prod, precio, stock):
    """
   \n `Uso:` Muestra un producto del inventario.
   \n `Entrada:` Nombre, precio y cantidad del producto.
   \n `Retorna:` Nada.
    """
    print("=====================================")
    print(f"Producto: {prod}")
    print("Precio: %5.2f" % precio)
    print(f"Stock: {stock}")