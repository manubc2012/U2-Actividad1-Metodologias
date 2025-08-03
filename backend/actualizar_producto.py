from backend.hoja_producto import obtener_hoja_de_productos
from backend.excel import guarda_hoja
from backend.crear_producto import buscar_producto_por_id

def actualizar_producto(id_producto, nombre=None, precio=None, cantidad=None):
    """
    Actualiza un producto existente
    
    Args:
        id_producto (int): ID del producto a actualizar
        nombre (str, optional): Nuevo nombre del producto
        precio (float, optional): Nuevo precio del producto
        cantidad (int, optional): Nueva cantidad del producto
        
    Returns:
        bool: True si se actualizó exitosamente, False si no se encontró el producto
    """
    hoja = obtener_hoja_de_productos()
    
    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4):
        if fila[0].value == id_producto:
            if nombre is not None:
                fila[1].value = nombre
            if precio is not None:
                fila[2].value = precio
            if cantidad is not None:
                fila[3].value = cantidad
            
            guarda_hoja(hoja)
            return True
    
    return False

def actualizar_producto_completo(id_producto, nombre, precio, cantidad):
    """
    Actualiza todos los campos de un producto
    
    Args:
        id_producto (int): ID del producto a actualizar
        nombre (str): Nuevo nombre del producto
        precio (float): Nuevo precio del producto
        cantidad (int): Nueva cantidad del producto
        
    Returns:
        bool: True si se actualizó exitosamente, False si no se encontró el producto
    """
    return actualizar_producto(id_producto, nombre, precio, cantidad)
