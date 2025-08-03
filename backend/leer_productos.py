from backend.hoja_producto import obtener_hoja_de_productos

def listar_productos():
    hoja = obtener_hoja_de_productos()
    productos = []

    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4):
        id_, nombre, precio, cantidad = [celda.value for celda in fila]

        producto = {
            "Id": id_,
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad
        }

        productos.append(producto)

    return productos
