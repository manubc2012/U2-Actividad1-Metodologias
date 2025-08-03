from backend.leer_productos import listar_productos
from backend.crear_producto import agregar_producto, obtener_siguiente_id, buscar_producto_por_id
from backend.actualizar_producto import actualizar_producto_completo
from backend.eliminar_producto import eliminar_producto
from tabulate import tabulate

def mostrar_productos():
    """Muestra todos los productos en una tabla formateada"""
    productos = listar_productos()

    if productos:
        print("\n" + "="*50)
        print("          LISTADO DE PRODUCTOS")
        print("="*50)
        print(tabulate(productos, headers="keys", tablefmt="fancy_grid"))
        print(f"\nTotal de productos: {len(productos)}")
    else:
        print("\nNo hay productos registrados o la hoja está vacía.")

def vista_buscar_producto():
    """Vista para buscar un producto específico"""
    print("\n" + "="*50)
    print("           BUSCAR PRODUCTO")
    print("="*50)
    
    try:
        id_producto = int(input("ID del producto a buscar: "))
    except ValueError:
        print("Error: Ingrese un ID válido.")
        return
    
    producto = buscar_producto_por_id(id_producto)
    if producto:
        producto_mostrar = {k: v for k, v in producto.items() if k != 'fila'}
        print(f"\nProducto encontrado:")
        print(tabulate([producto_mostrar], headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró un producto con ID {id_producto}")

def vista_agregar_producto():
    """Vista para agregar un nuevo producto"""
    print("\n" + "="*50)
    print("           AGREGAR NUEVO PRODUCTO")
    print("="*50)
    
    try:
        id_str = input("ID del producto (o Enter para generar automáticamente): ").strip()
        if id_str == "":
            id_producto = obtener_siguiente_id()
            print(f"ID generado automáticamente: {id_producto}")
        else:
            id_producto = int(id_str)
        
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
        
        cantidad = int(input("Cantidad en inventario: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        
        if agregar_producto(id_producto, nombre, precio, cantidad):
            print(f"\nProducto agregado exitosamente!")
            print(f"   ID: {id_producto}")
            print(f"   Nombre: {nombre}")
            print(f"   Precio: ${precio:.2f}")
            print(f"   Cantidad: {cantidad}")
        else:
            print(f"\nError: Ya existe un producto con ID {id_producto}")
    
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")

def vista_actualizar_producto():
    """Vista para actualizar un producto existente"""
    print("\n" + "="*50)
    print("           ACTUALIZAR PRODUCTO")
    print("="*50)
    
    try:
        id_producto = int(input("ID del producto a actualizar: "))
    except ValueError:
        print("Error: Ingrese un ID válido.")
        return
    
    producto_actual = buscar_producto_por_id(id_producto)
    if not producto_actual:
        print(f"No se encontró un producto con ID {id_producto}")
        return
    
    print(f"\nDatos actuales del producto:")
    print(f"  ID: {producto_actual['Id']}")
    print(f"  Nombre: {producto_actual['Nombre']}")
    print(f"  Precio: ${producto_actual['Precio']}")
    print(f"  Cantidad: {producto_actual['Cantidad']}")
    
    print(f"\n¿Qué desea actualizar?")
    print("1. Nombre")
    print("2. Precio")
    print("3. Cantidad")
    print("4. Todos los campos")
    print("5. Cancelar")
    
    try:
        opcion_actualizar = input("Seleccione una opción (1-5): ").strip()
    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        return
    
    nuevo_nombre = producto_actual['Nombre']
    nuevo_precio = producto_actual['Precio']
    nueva_cantidad = producto_actual['Cantidad']
    
    if opcion_actualizar == "1":
        try:
            nuevo_nombre = input(f"Nuevo nombre [{producto_actual['Nombre']}]: ").strip()
            if nuevo_nombre == "":
                nuevo_nombre = producto_actual['Nombre']
            elif not nuevo_nombre:
                print("El nombre no puede estar vacío.")
                return
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return
            
    elif opcion_actualizar == "2":
        try:
            precio_str = input(f"Nuevo precio [{producto_actual['Precio']}]: ").strip()
            if precio_str == "":
                nuevo_precio = producto_actual['Precio']
            else:
                nuevo_precio = float(precio_str)
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    return
        except ValueError:
            print("Error: Ingrese un precio válido.")
            return
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return
            
    elif opcion_actualizar == "3":
        try:
            cantidad_str = input(f"Nueva cantidad [{producto_actual['Cantidad']}]: ").strip()
            if cantidad_str == "":
                nueva_cantidad = producto_actual['Cantidad']
            else:
                nueva_cantidad = int(cantidad_str)
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return
        except ValueError:
            print("Error: Ingrese una cantidad válida.")
            return
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return
            
    elif opcion_actualizar == "4":
        try:
            print(f"\nIngrese los nuevos datos (Enter para mantener el valor actual):")
            
            nuevo_nombre = input(f"Nuevo nombre [{producto_actual['Nombre']}]: ").strip()
            if nuevo_nombre == "":
                nuevo_nombre = producto_actual['Nombre']
            elif not nuevo_nombre:
                print("El nombre no puede estar vacío.")
                return
            
            precio_str = input(f"Nuevo precio [{producto_actual['Precio']}]: ").strip()
            if precio_str == "":
                nuevo_precio = producto_actual['Precio']
            else:
                nuevo_precio = float(precio_str)
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    return
            
            cantidad_str = input(f"Nueva cantidad [{producto_actual['Cantidad']}]: ").strip()
            if cantidad_str == "":
                nueva_cantidad = producto_actual['Cantidad']
            else:
                nueva_cantidad = int(cantidad_str)
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return
        except ValueError:
            print("Error: Ingrese valores válidos.")
            return
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return
            
    elif opcion_actualizar == "5":
        print("\nActualización cancelada.")
        return
    else:
        print("\nOpción inválida.")
        return
    
    if actualizar_producto_completo(id_producto, nuevo_nombre, nuevo_precio, nueva_cantidad):
        print(f"\nProducto actualizado exitosamente!")
        print(f"   ID: {id_producto}")
        print(f"   Nombre: {nuevo_nombre}")
        print(f"   Precio: ${nuevo_precio:.2f}")
        print(f"   Cantidad: {nueva_cantidad}")
    else:
        print(f"\nError al actualizar el producto.")

def vista_eliminar_producto():
    """Vista para eliminar un producto"""
    print("\n" + "="*50)
    print("           ELIMINAR PRODUCTO")
    print("="*50)
    
    try:
        id_producto = int(input("ID del producto a eliminar: "))
    except ValueError:
        print("Error: Ingrese un ID válido.")
        return
    
    producto = buscar_producto_por_id(id_producto)
    if not producto:
        print(f"No se encontró un producto con ID {id_producto}")
        return
    
    print(f"\nProducto a eliminar:")
    print(f"  ID: {producto['Id']}")
    print(f"  Nombre: {producto['Nombre']}")
    print(f"  Precio: ${producto['Precio']}")
    print(f"  Cantidad: {producto['Cantidad']}")
    
    confirmacion = input("\n¿Está seguro de que desea eliminar este producto? (s/n): ").lower().strip()
    
    if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
        if eliminar_producto(id_producto):
            print(f"\nProducto eliminado exitosamente!")
        else:
            print(f"\nError al eliminar el producto.")
    else:
        print("\nEliminación cancelada.")

def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n" + "="*60)
    print("        SISTEMA DE GESTIÓN DE PRODUCTOS - CRUD")
    print("="*60)
    print("1. Listar todos los productos")
    print("2. Buscar producto por ID") 
    print("3. Agregar nuevo producto")
    print("4. Actualizar producto existente")
    print("5. Eliminar producto")
    print("6. Salir")
    print("-"*60)

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada por el usuario"""
    if opcion == "1":
        mostrar_productos()
    elif opcion == "2":
        vista_buscar_producto()
    elif opcion == "3":
        vista_agregar_producto()
    elif opcion == "4":
        vista_actualizar_producto()
    elif opcion == "5":
        vista_eliminar_producto()
    elif opcion == "6":
        print("\nGracias por usar el sistema!")
        return False
    else:
        print("\nOpción inválida. Por favor, seleccione un número del 1 al 6.")
    
    return True

def iniciar_aplicacion():
    """Función principal que ejecuta el menú de la aplicación"""
    continuar = True
    
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        continuar = ejecutar_opcion(opcion)
        
        if continuar:
            input("\nPresione Enter para continuar...")
