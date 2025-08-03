from backend.hoja_producto import obtener_hoja_de_productos
from backend.excel import guarda_hoja
from backend.crear_producto import buscar_producto_por_id

def eliminar_producto(id_producto):
    """
    Elimina un producto del archivo Excel
    
    Args:
        id_producto (int): ID del producto a eliminar
        
    Returns:
        bool: True si se eliminó exitosamente, False si no se encontró el producto
    """
    hoja = obtener_hoja_de_productos()
    
    for fila in hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=1):
        if fila[0].value == id_producto:
            hoja.delete_rows(fila[0].row)
            guarda_hoja(hoja)
            return True
    
    return False

def eliminar_todos_los_productos():
    """
    Elimina todos los productos (mantiene solo las cabeceras)
    
    Returns:
        int: Número de productos eliminados
    """
    hoja = obtener_hoja_de_productos()
    productos_eliminados = 0
    
    if hoja.max_row > 1:
        productos_eliminados = hoja.max_row - 1
        
        hoja.delete_rows(2, hoja.max_row - 1)
        guarda_hoja(hoja)
    
    return productos_eliminados
