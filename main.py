from frontend.menu import iniciar_aplicacion

def main():
    """
    Función principal que inicia la aplicación de gestión de productos
    """
    try:
        iniciar_aplicacion()
    except KeyboardInterrupt:
        print("\n\nAplicación cerrada por el usuario!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("Por favor, contacte al administrador del sistema.")

if __name__ == "__main__":
    main()

