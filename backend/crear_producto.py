from backend.hoja_producto import obtener_hoja_de_productos
from backend.excel import guarda_hoja

def agregar_producto(id_producto, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al archivo Excel
    
    Args:
        id_producto (int): ID único del producto
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        cantidad (int): Cantidad en inventario
        
    Returns:
        bool: True si se agregó exitosamente, False si ya existe el ID
    """
    hoja = obtener_hoja_de_productos()
    
    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=1):
        if fila[0].value == id_producto:
            return False
    
    hoja.append([id_producto, nombre, precio, cantidad])
    guarda_hoja(hoja)
    return True

def obtener_siguiente_id():
    """
    Obtiene el siguiente ID disponible para un nuevo producto
    
    Returns:
        int: El siguiente ID disponible
    """
    hoja = obtener_hoja_de_productos()
    max_id = 0
    
    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=1):
        if fila[0].value and isinstance(fila[0].value, (int, float)):
            max_id = max(max_id, int(fila[0].value))
    
    return max_id + 1

def buscar_producto_por_id(id_producto):
    """
    Busca un producto por su ID
    
    Args:
        id_producto (int): ID del producto a buscar
        
    Returns:
        dict or None: Diccionario con los datos del producto o None si no existe
    """
    hoja = obtener_hoja_de_productos()
    
    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4):
        id_, nombre, precio, cantidad = [celda.value for celda in fila]
        
        if id_ == id_producto:
            return {
                "Id": id_,
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad,
                "fila": fila[0].row
            }
    
    return None
