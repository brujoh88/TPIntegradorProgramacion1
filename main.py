# Sistema de Gestión de Inventario - Supermercado (Versión Simplificada)
# Algoritmos de Búsqueda y Ordenamiento en Python
# Alumnos: Tiseira Gustavo Hernan, Trejo Daiana Anahi

import time
from productos import agregar_productos_ejemplo, mostrar_productos, mostrar_productos_stock_bajo
from ordenamiento import bubble_sort, selection_sort
from busqueda import busqueda_lineal, busqueda_binaria

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("   SISTEMA DE INVENTARIO - SUPERMERCADO")
    print("="*50)
    print("1. Ver todos los productos")
    print("2. Ordenar productos por precio (Bubble Sort)")
    print("3. Ordenar productos por stock (Selection Sort)")
    print("4. Buscar producto por código (Búsqueda Lineal)")
    print("5. Buscar producto por código (Búsqueda Binaria)")
    print("6. Buscar producto por nombre")
    print("7. Ver productos con stock bajo")
    print("8. Comparar velocidad de algoritmos")
    print("9. Salir")
    print("="*50)

def comparar_algoritmos(productos):
    """Compara la velocidad de los algoritmos de ordenamiento"""
    print("\n--- COMPARACIÓN DE ALGORITMOS ---")
    
    # Crear copias para no modificar la lista original
    productos_bubble = productos.copy()
    productos_selection = productos.copy()
    
    # Medir Bubble Sort
    inicio = time.time()
    bubble_sort(productos_bubble, 'precio')
    tiempo_bubble = time.time() - inicio
    
    # Medir Selection Sort
    inicio = time.time()
    selection_sort(productos_selection, 'stock')
    tiempo_selection = time.time() - inicio
    
    print(f"Bubble Sort (por precio): {tiempo_bubble:.6f} segundos")
    print(f"Selection Sort (por stock): {tiempo_selection:.6f} segundos")

def main():
    """Función principal del programa"""
    # Crear lista de productos con datos de ejemplo
    productos = agregar_productos_ejemplo()
    
    print("¡Bienvenido al Sistema de Inventario!")
    print("Se han cargado productos de ejemplo.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSeleccione una opción (1-9): "))
            
            if opcion == 1:
                print("\n--- LISTA COMPLETA DE PRODUCTOS ---")
                mostrar_productos(productos)
                
            elif opcion == 2:
                print("\n--- ORDENANDO POR PRECIO (BUBBLE SORT) ---")
                inicio = time.time()
                bubble_sort(productos, 'precio')
                tiempo = time.time() - inicio
                print(f"Ordenamiento completado en {tiempo:.6f} segundos")
                mostrar_productos(productos)
                
            elif opcion == 3:
                print("\n--- ORDENANDO POR STOCK (SELECTION SORT) ---")
                inicio = time.time()
                selection_sort(productos, 'stock')
                tiempo = time.time() - inicio
                print(f"Ordenamiento completado en {tiempo:.6f} segundos")
                mostrar_productos(productos)
                
            elif opcion == 4:
                codigo = input("\nIngrese el código del producto a buscar: ")
                print("\n--- BÚSQUEDA LINEAL ---")
                inicio = time.time()
                resultado = busqueda_lineal(productos, codigo)
                tiempo = time.time() - inicio
                
                if resultado != -1:
                    producto = productos[resultado]
                    print(f"Código: {producto['codigo']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio: ${producto['precio']}")
                    print(f"Stock: {producto['stock']} unidades")
                print(f"Búsqueda completada en {tiempo:.6f} segundos")
                
            elif opcion == 5:
                codigo = input("\nIngrese el código del producto a buscar: ")
                print("\n--- BÚSQUEDA BINARIA ---")
                # Primero ordenamos por código para poder usar búsqueda binaria
                productos_ordenados = sorted(productos, key=lambda x: x['codigo'])
                
                inicio = time.time()
                resultado = busqueda_binaria(productos_ordenados, codigo)
                tiempo = time.time() - inicio
                
                if resultado != -1:
                    producto = productos_ordenados[resultado]
                    print(f"Código: {producto['codigo']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio: ${producto['precio']}")
                    print(f"Stock: {producto['stock']} unidades")
                print(f"Búsqueda completada en {tiempo:.6f} segundos")
                
            elif opcion == 6:
                nombre = input("\nIngrese el nombre del producto a buscar: ").lower()
                print("\n--- BÚSQUEDA POR NOMBRE ---")
                encontrados = []
                for i, producto in enumerate(productos):
                    if nombre in producto['nombre'].lower():
                        encontrados.append(producto)
                
                if encontrados:
                    print(f"Se encontraron {len(encontrados)} producto(s):")
                    for producto in encontrados:
                        print(f"- {producto['codigo']}: {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")
                else:
                    print("No se encontraron productos con ese nombre.")
                    
            elif opcion == 7:
                print("\n--- PRODUCTOS CON STOCK BAJO ---")
                mostrar_productos_stock_bajo(productos)
                
            elif opcion == 8:
                comparar_algoritmos(productos)
                
            elif opcion == 9:
                print("\n¡Gracias por usar el sistema!")
                print("Desarrollado por: Tiseira Gustavo y Trejo Daiana")
                break
                
            else:
                print("\nOpción no válida. Por favor ingrese un número del 1 al 9.")
                
        except ValueError:
            print("\nError: Por favor ingrese un número válido.")
        except Exception as e:
            print(f"\nError inesperado: {e}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()