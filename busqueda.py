# busqueda.py - Algoritmos de búsqueda

def busqueda_lineal(productos, codigo_buscado):
    """
    Algoritmo de Búsqueda Lineal (Secuencial)
    Busca un producto por código recorriendo toda la lista elemento por elemento
    
    Parámetros:
    - productos: lista de diccionarios con los productos
    - codigo_buscado: código del producto a buscar
    
    Retorna:
    - índice del producto si lo encuentra
    - -1 si no lo encuentra
    """
    print(f"Buscando producto con código '{codigo_buscado}'...")
    
    # Recorremos toda la lista elemento por elemento
    for i in range(len(productos)):
        print(f"Revisando posición {i}: {productos[i]['codigo']}")
        
        # Si encontramos el código, retornamos la posición
        if productos[i]['codigo'] == codigo_buscado:
            print(f"¡Producto encontrado en la posición {i}!")
            return i
    
    # Si llegamos aquí, no encontramos el producto
    print("Producto no encontrado.")
    return -1

def busqueda_binaria(productos_ordenados, codigo_buscado):
    """
    Algoritmo de Búsqueda Binaria
    Busca un producto por código en una lista ordenada
    Divide la lista por la mitad en cada iteración
    
    IMPORTANTE: La lista debe estar ordenada por código
    
    Parámetros:
    - productos_ordenados: lista ordenada de productos por código
    - codigo_buscado: código del producto a buscar
    
    Retorna:
    - índice del producto si lo encuentra
    - -1 si no lo encuentra
    """
    print(f"Buscando producto con código '{codigo_buscado}' (Búsqueda Binaria)...")
    
    izquierda = 0
    derecha = len(productos_ordenados) - 1
    
    while izquierda <= derecha:
        # Calculamos el punto medio
        medio = (izquierda + derecha) // 2
        codigo_medio = productos_ordenados[medio]['codigo']
        
        print(f"Revisando posición {medio}: código {codigo_medio}")
        
        # Si encontramos el código
        if codigo_medio == codigo_buscado:
            print(f"¡Producto encontrado en la posición {medio}!")
            return medio
        
        # Si el código buscado es menor, buscamos en la mitad izquierda
        elif codigo_buscado < codigo_medio:
            print(f"El código buscado es menor que {codigo_medio}, buscando en la mitad izquierda")
            derecha = medio - 1
        
        # Si el código buscado es mayor, buscamos en la mitad derecha
        else:
            print(f"El código buscado es mayor que {codigo_medio}, buscando en la mitad derecha")
            izquierda = medio + 1
    
    # Si llegamos aquí, no encontramos el producto
    print("Producto no encontrado.")
    return -1