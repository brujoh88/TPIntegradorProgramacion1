# productos.py - Gestión de productos del supermercado

def crear_producto(codigo, nombre, precio, stock):
    """
    Crea un diccionario que representa un producto
    """
    return {
        'codigo': codigo,
        'nombre': nombre,
        'precio': precio,
        'stock': stock
    }

def agregar_productos_ejemplo():
    """
    Crea una lista con productos de ejemplo para el supermercado
    """
    productos = []
    
    # Agregamos productos típicos de supermercado
    productos.append(crear_producto("001", "Leche Entera 1L", 150.50, 25))
    productos.append(crear_producto("002", "Pan Lactal", 89.99, 40))
    productos.append(crear_producto("003", "Arroz 1kg", 120.00, 15))
    productos.append(crear_producto("004", "Fideos 500g", 95.75, 30))
    productos.append(crear_producto("005", "Aceite Girasol 900ml", 185.30, 8))
    productos.append(crear_producto("006", "Azúcar 1kg", 98.50, 20))
    productos.append(crear_producto("007", "Café Molido 250g", 425.00, 12))
    productos.append(crear_producto("008", "Shampoo 400ml", 320.75, 18))
    productos.append(crear_producto("009", "Detergente 750ml", 175.90, 22))
    productos.append(crear_producto("010", "Yerba Mate 1kg", 890.00, 35))
    productos.append(crear_producto("011", "Galletitas Dulces", 125.50, 45))
    productos.append(crear_producto("012", "Manteca 200g", 145.75, 28))
    productos.append(crear_producto("013", "Huevos x12", 180.00, 50))
    productos.append(crear_producto("014", "Papel Higiénico x4", 220.30, 32))
    productos.append(crear_producto("015", "Atún en Lata", 195.80, 24))
    
    return productos

def mostrar_productos(productos):
    """
    Muestra todos los productos de la lista de forma organizada
    """
    if not productos:
        print("No hay productos en el inventario.")
        return
    
    print(f"{'Código':<8} {'Nombre':<20} {'Precio':<10} {'Stock':<8}")
    print("-" * 50)
    
    for producto in productos:
        print(f"{producto['codigo']:<8} {producto['nombre']:<20} ${producto['precio']:<9.2f} {producto['stock']:<8}")
    
    print(f"\nTotal de productos: {len(productos)}")

def mostrar_productos_stock_bajo(productos, limite=10):
    """
    Muestra productos con stock por debajo del límite especificado
    """
    productos_bajo_stock = []
    
    for producto in productos:
        if producto['stock'] <= limite:
            productos_bajo_stock.append(producto)
    
    if productos_bajo_stock:
        print(f"Productos con stock menor o igual a {limite} unidades:")
        print(f"{'Código':<8} {'Nombre':<20} {'Precio':<10} {'Stock':<8}")
        print("-" * 50)
        
        for producto in productos_bajo_stock:
            print(f"{producto['codigo']:<8} {producto['nombre']:<20} ${producto['precio']:<9.2f} {producto['stock']:<8}")
        
        print(f"\n¡ATENCIÓN! {len(productos_bajo_stock)} producto(s) necesitan reposición.")
    else:
        print(f"Todos los productos tienen stock superior a {limite} unidades.")