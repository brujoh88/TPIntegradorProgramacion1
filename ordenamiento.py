# ordenamiento.py - Algoritmos de ordenamiento

def bubble_sort(productos, criterio):
    """
    Algoritmo Bubble Sort (Ordenamiento Burbuja)
    Ordena la lista de productos según el criterio especificado
    
    Parámetros:
    - productos: lista de diccionarios con los productos
    - criterio: 'precio', 'stock', 'nombre' o 'codigo'
    """
    n = len(productos)
    
    # Realizamos n-1 pasadas
    for i in range(n - 1):
        # Variable para optimizar: si no hay intercambios, la lista ya está ordenada
        hubo_intercambio = False
        
        # En cada pasada, comparamos elementos adyacentes
        for j in range(n - 1 - i):
            # Comparamos según el criterio especificado
            if productos[j][criterio] > productos[j + 1][criterio]:
                # Intercambiamos los elementos
                productos[j], productos[j + 1] = productos[j + 1], productos[j]
                hubo_intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            break
    
    print(f"Bubble Sort completado. Lista ordenada por {criterio}.")

def selection_sort(productos, criterio):
    """
    Algoritmo Selection Sort (Ordenamiento por Selección)
    Ordena la lista de productos según el criterio especificado
    
    Parámetros:
    - productos: lista de diccionarios con los productos
    - criterio: 'precio', 'stock', 'nombre' o 'codigo'
    """
    n = len(productos)
    
    # Recorremos toda la lista
    for i in range(n - 1):
        # Asumimos que el elemento actual es el mínimo
        indice_minimo = i
        
        # Buscamos el elemento mínimo en el resto de la lista
        for j in range(i + 1, n):
            if productos[j][criterio] < productos[indice_minimo][criterio]:
                indice_minimo = j
        
        # Si encontramos un elemento menor, lo intercambiamos
        if indice_minimo != i:
            productos[i], productos[indice_minimo] = productos[indice_minimo], productos[i]
    
    print(f"Selection Sort completado. Lista ordenada por {criterio}.")