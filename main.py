from backend.leer_productos import listar_productos
from tabulate import tabulate
def mostrar_productos():
    productos = listar_productos()

    if productos:
        print("\n=== LISTADO DE PRODUCTOS ===")
        print(tabulate(productos, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No hay productos registrados o la hoja está vacía.")

def main():
    mostrar_productos()

if __name__ == "__main__":
    main()

