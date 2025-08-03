"""
Pruebas completas del sistema CRUD de gestión de productos
"""

from backend.leer_productos import listar_productos
from backend.crear_producto import agregar_producto, obtener_siguiente_id, buscar_producto_por_id
from backend.actualizar_producto import actualizar_producto_completo, actualizar_producto
from backend.eliminar_producto import eliminar_producto

def mostrar_productos_simple(productos):
    """Muestra productos de forma simple"""
    for producto in productos:
        print(f"   ID: {producto['Id']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}")

def probar_crud_basico():
    """Prueba básica del funcionamiento CRUD"""
    print("PRUEBAS CRUD BASICAS")
    print("=" * 50)
    
    # 1. Mostrar productos existentes
    print("\n1. PRODUCTOS INICIALES:")
    productos_iniciales = listar_productos()
    print(f"Total de productos: {len(productos_iniciales)}")
    mostrar_productos_simple(productos_iniciales)
    
    # 2. Crear un producto de prueba
    print("\n2. CREANDO PRODUCTO DE PRUEBA:")
    siguiente_id = obtener_siguiente_id()
    nombre = "Producto Test"
    precio = 50.0
    cantidad = 5
    
    resultado_crear = agregar_producto(siguiente_id, nombre, precio, cantidad)
    if resultado_crear:
        print(f"Producto creado exitosamente - ID: {siguiente_id}")
    else:
        print("Error al crear producto")
        return False
    
    # 3. Verificar que se creó
    print("\n3. VERIFICANDO CREACION:")
    producto_creado = buscar_producto_por_id(siguiente_id)
    if producto_creado:
        print(f"Producto encontrado: {producto_creado['Nombre']}")
    else:
        print("Producto no encontrado")
        return False
    
    # 4. Actualizar el producto completo
    print("\n4. ACTUALIZANDO PRODUCTO COMPLETO:")
    nuevo_nombre = "Producto Modificado"
    nuevo_precio = 75.0
    nueva_cantidad = 8
    
    resultado_actualizar = actualizar_producto_completo(siguiente_id, nuevo_nombre, nuevo_precio, nueva_cantidad)
    if resultado_actualizar:
        print("Producto actualizado exitosamente")
        producto_actualizado = buscar_producto_por_id(siguiente_id)
        print(f"Nuevos datos: {producto_actualizado['Nombre']}, Precio: {producto_actualizado['Precio']}")
    else:
        print("Error al actualizar producto")
        return False
    
    # 5. Eliminar el producto de prueba
    print("\n5. ELIMINANDO PRODUCTO DE PRUEBA:")
    resultado_eliminar = eliminar_producto(siguiente_id)
    if resultado_eliminar:
        print(f"Producto ID {siguiente_id} eliminado exitosamente")
    else:
        print("Error al eliminar producto")
        return False
    
    # 6. Verificar eliminación
    print("\n6. VERIFICANDO ELIMINACION:")
    producto_eliminado = buscar_producto_por_id(siguiente_id)
    if producto_eliminado is None:
        print("Confirmado: Producto eliminado correctamente")
    else:
        print("Error: El producto aún existe")
        return False
    
    # 7. Estado final
    print("\n7. ESTADO FINAL:")
    productos_finales = listar_productos()
    print(f"Total de productos: {len(productos_finales)}")
    if len(productos_finales) == len(productos_iniciales):
        print("Base de datos restaurada al estado inicial")
    
    return True

def probar_actualizacion_selectiva():
    """Prueba la funcionalidad de actualización campo por campo"""
    print("\n" + "=" * 50)
    print("PRUEBAS DE ACTUALIZACION SELECTIVA")
    print("=" * 50)
    
    # 1. Crear un producto de prueba
    print("\n1. CREANDO PRODUCTO PARA ACTUALIZACION SELECTIVA:")
    siguiente_id = obtener_siguiente_id()
    nombre_original = "Producto Original"
    precio_original = 100.0
    cantidad_original = 10
    
    if agregar_producto(siguiente_id, nombre_original, precio_original, cantidad_original):
        print(f"Producto creado - ID: {siguiente_id}")
        print(f"   Nombre: {nombre_original}")
        print(f"   Precio: {precio_original}")
        print(f"   Cantidad: {cantidad_original}")
    else:
        print("Error al crear producto")
        return False
    
    # 2. Actualizar solo el nombre
    print("\n2. ACTUALIZANDO SOLO EL NOMBRE:")
    nuevo_nombre = "Producto Renombrado"
    if actualizar_producto(siguiente_id, nombre=nuevo_nombre):
        producto = buscar_producto_por_id(siguiente_id)
        print(f"Nombre actualizado exitosamente:")
        print(f"   Nombre: {producto['Nombre']} (cambiado)")
        print(f"   Precio: {producto['Precio']} (sin cambios)")
        print(f"   Cantidad: {producto['Cantidad']} (sin cambios)")
    else:
        print("Error al actualizar nombre")
        return False
    
    # 3. Actualizar solo el precio
    print("\n3. ACTUALIZANDO SOLO EL PRECIO:")
    nuevo_precio = 150.0
    if actualizar_producto(siguiente_id, precio=nuevo_precio):
        producto = buscar_producto_por_id(siguiente_id)
        print(f"Precio actualizado exitosamente:")
        print(f"   Nombre: {producto['Nombre']} (sin cambios)")
        print(f"   Precio: {producto['Precio']} (cambiado)")
        print(f"   Cantidad: {producto['Cantidad']} (sin cambios)")
    else:
        print("Error al actualizar precio")
        return False
    
    # 4. Actualizar solo la cantidad
    print("\n4. ACTUALIZANDO SOLO LA CANTIDAD:")
    nueva_cantidad = 25
    if actualizar_producto(siguiente_id, cantidad=nueva_cantidad):
        producto = buscar_producto_por_id(siguiente_id)
        print(f"Cantidad actualizada exitosamente:")
        print(f"   Nombre: {producto['Nombre']} (sin cambios)")
        print(f"   Precio: {producto['Precio']} (sin cambios)")
        print(f"   Cantidad: {producto['Cantidad']} (cambiado)")
    else:
        print("Error al actualizar cantidad")
        return False
    
    # 5. Mostrar estado final del producto
    print("\n5. ESTADO FINAL DEL PRODUCTO:")
    producto_final = buscar_producto_por_id(siguiente_id)
    print(f"   ID: {producto_final['Id']}")
    print(f"   Nombre: {producto_final['Nombre']}")
    print(f"   Precio: {producto_final['Precio']}")
    print(f"   Cantidad: {producto_final['Cantidad']}")
    
    # 6. Limpiar - eliminar el producto de prueba
    print("\n6. ELIMINANDO PRODUCTO DE PRUEBA:")
    if eliminar_producto(siguiente_id):
        print("Producto eliminado correctamente")
        return True
    else:
        print("Error al eliminar producto")
        return False

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema"""
    print("SISTEMA DE PRUEBAS COMPLETO")
    print("=" * 60)
    
    try:
        # Ejecutar pruebas CRUD básicas
        exito_crud = probar_crud_basico()
        
        if exito_crud:
            # Ejecutar pruebas de actualización selectiva
            exito_actualizacion = probar_actualizacion_selectiva()
            
            if exito_actualizacion:
                print("\n" + "=" * 60)
                print("TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
                print("=" * 60)
            else:
                print("\nError en las pruebas de actualización selectiva")
        else:
            print("\nError en las pruebas CRUD básicas")
            
    except Exception as e:
        print(f"\nERROR DURANTE LAS PRUEBAS: {e}")

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
