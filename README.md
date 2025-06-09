# 🏪 Sistema de Gestión de Inventario - Supermercado

**Algoritmos de Búsqueda y Ordenamiento en Python**

---

## 👥 Autores
- **Tiseira Gustavo Hernan**
- **Trejo Daiana Anahi**

**Materia:** Programación I  
**Profesora:** Martina Wallace  
**Tutor:** Walter Pintos  
**Fecha de Entrega:** 09/06/2025

---

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de gestión de inventario para supermercado utilizando **programación estructurada** en Python. El sistema demuestra la aplicación práctica de algoritmos fundamentales de búsqueda y ordenamiento en un contexto real y familiar.

### 🎯 Objetivos
- Implementar algoritmos básicos de ordenamiento (Bubble Sort, Selection Sort)
- Desarrollar algoritmos de búsqueda (lineal y binaria)
- Crear un sistema práctico de gestión usando programación estructurada
- Comparar la eficiencia de diferentes algoritmos
- Aplicar conceptos de funciones y modularización en Python

---

## 🚀 Características Principales

### Algoritmos de Ordenamiento
- **Bubble Sort:** Ordenamiento por precio con visualización del proceso
- **Selection Sort:** Ordenamiento por stock con optimización de intercambios

### Algoritmos de Búsqueda
- **Búsqueda Lineal:** Búsqueda secuencial por código de producto
- **Búsqueda Binaria:** Búsqueda optimizada en listas ordenadas
- **Búsqueda por Nombre:** Búsqueda parcial de productos
- **Búsqueda por Rango:** Filtros por precio y stock

### Funcionalidades del Sistema
- ✅ Visualización completa del inventario
- ✅ Ordenamiento por múltiples criterios
- ✅ Búsqueda rápida de productos
- ✅ Identificación de productos con stock bajo
- ✅ Comparación de rendimiento entre algoritmos
- ✅ Interfaz de usuario intuitiva mediante menú

---

## 📁 Estructura del Proyecto

```
sistema-inventario/
│
├── main.py              # Programa principal con interfaz de usuario
├── productos.py         # Gestión de productos y datos de ejemplo
├── ordenamiento.py      # Algoritmos de ordenamiento
├── busqueda.py         # Algoritmos de búsqueda
├── README.md           # Documentación del proyecto
└── informe.pdf         # Informe técnico completo
```

### Descripción de Archivos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Contiene el menú principal y la lógica de interacción con el usuario |
| `productos.py` | Funciones para crear productos, generar datos de ejemplo y mostrar información |
| `ordenamiento.py` | Implementación de Bubble Sort y Selection Sort |
| `busqueda.py` | Implementación de búsqueda lineal, binaria y búsquedas especializadas |

---

## 🛠️ Instalación y Uso

### Requisitos
- Python 3.6 o superior
- No requiere librerías externas

### Instalación
1. Clona o descarga el repositorio
2. Navega al directorio del proyecto
3. Ejecuta el programa principal

```bash
# Clonar el repositorio
git clone [URL-del-repositorio]

# Navegar al directorio
cd sistema-inventario

# Ejecutar el programa
python main.py
```

### Uso del Sistema
1. Al ejecutar `main.py`, se cargan automáticamente 15 productos de ejemplo
2. Utiliza el menú interactivo para navegar por las opciones
3. Todas las operaciones incluyen medición de tiempo de ejecución
4. El sistema muestra el proceso paso a paso de cada algoritmo

---

## 🎮 Menú de Opciones

```
===============================================
   SISTEMA DE INVENTARIO - SUPERMERCADO
===============================================
1. Ver todos los productos
2. Ordenar productos por precio (Bubble Sort)
3. Ordenar productos por stock (Selection Sort)
4. Buscar producto por código (Búsqueda Lineal)
5. Buscar producto por código (Búsqueda Binaria)
6. Buscar producto por nombre
7. Ver productos con stock bajo
8. Comparar velocidad de algoritmos
9. Salir
===============================================
```

---

## 📊 Algoritmos Implementados

### Ordenamiento

#### Bubble Sort
- **Complejidad:** O(n²)
- **Uso:** Ordenamiento por precio
- **Características:** Fácil implementación, visualización clara del proceso

```python
def bubble_sort(productos, criterio):
    n = len(productos)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if productos[j][criterio] > productos[j + 1][criterio]:
                productos[j], productos[j + 1] = productos[j + 1], productos[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
```

#### Selection Sort
- **Complejidad:** O(n²)
- **Uso:** Ordenamiento por stock
- **Características:** Menos intercambios que Bubble Sort

### Búsqueda

#### Búsqueda Lineal
- **Complejidad:** O(n)
- **Ventaja:** Funciona con listas ordenadas y desordenadas
- **Uso:** Búsqueda general por código

#### Búsqueda Binaria
- **Complejidad:** O(log n)
- **Requisito:** Lista ordenada
- **Ventaja:** Mucho más eficiente para listas grandes

---

## 📈 Rendimiento

### Resultados con 15 productos (tiempos aproximados):
- **Bubble Sort:** ~0.000015 segundos
- **Selection Sort:** ~0.000012 segundos
- **Búsqueda Lineal:** ~0.000008 segundos
- **Búsqueda Binaria:** ~0.000003 segundos

> **Nota:** Los tiempos pueden variar según el hardware utilizado

---

## 🧪 Casos de Prueba

El sistema incluye casos de prueba para:
- ✅ Ordenamiento con diferentes cantidades de productos
- ✅ Búsqueda de productos existentes y no existentes
- ✅ Búsqueda por nombre parcial
- ✅ Identificación de productos con stock bajo
- ✅ Comparación de tiempos de ejecución

---

## 🤖 Uso de Inteligencia Artificial

**Metodología Híbrida:**
- **Desarrollo Autónomo:** Toda la lógica algorítmica y funcional fue desarrollada completamente por los estudiantes
- **Mejoras Estéticas:** Se utilizó IA generativa para:
  - Mejorar la presentación visual de menús
  - Optimizar comentarios y documentación
  - Estructurar mejor la organización del código

> La lógica fundamental de los algoritmos se mantuvo intacta y fue desarrollada sin asistencia de IA.

---

## 🔍 Ejemplos de Uso

### Búsqueda de Producto
```python
# Buscar producto por código
codigo = "001"
resultado = busqueda_lineal(productos, codigo)
# Output: Producto encontrado - Leche Entera 1L
```

### Ordenamiento por Precio
```python
# Ordenar productos por precio usando Bubble Sort
bubble_sort(productos, 'precio')
# Los productos se ordenan de menor a mayor precio
```

---

## 📚 Conceptos Aprendidos

### Programación Estructurada
- Uso de funciones para modularizar código
- Separación de responsabilidades
- Código reutilizable y mantenible

### Algoritmos
- Diferencias entre algoritmos de ordenamiento
- Importancia de la complejidad temporal
- Casos de uso apropiados para cada algoritmo

### Buenas Prácticas
- Documentación clara del código
- Manejo de errores
- Interfaz de usuario amigable

---

## 🚧 Posibles Mejoras

- [ ] Implementar algoritmos más eficientes (Quick Sort, Merge Sort)
- [ ] Agregar persistencia de datos en archivos
- [ ] Incluir más campos de producto (categoría, proveedor)
- [ ] Desarrollar interfaz gráfica
- [ ] Implementar manejo de excepciones más robusto
- [ ] Agregar funcionalidades de reportes

---

## 📖 Referencias

- Apuntes de Cátedra - Programación I (2025). Universidad Tecnológica Nacional
- Documentación oficial de Python: https://docs.python.org/es/3/tutorial/

---

**🎓 Universidad Tecnológica Nacional - 2025**