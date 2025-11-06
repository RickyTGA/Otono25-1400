# Ejemplos de Estructuras de Datos en Python

Esta carpeta contiene ejemplos completos de las principales estructuras de datos en Python.

## Archivos incluidos:

### 1. `listas_completo.py`
Ejemplos de **LISTAS** que incluyen:
- Crear listas con `[]`
- Usar `len()` para obtener longitud
- Acceso con índices positivos y negativos (`[-1]`)
- Slicing (`[1:3]`)
- Agregar elementos: `append()`, `insert()`, `extend()`
- Quitar elementos: `remove()`, `pop()`

### 2. `diccionario_completo.py`
Ejemplos de **DICCIONARIOS** que incluyen:
- Crear diccionarios con `{}`
- Acceso por claves
- Agregar y eliminar elementos
- Métodos: `keys()`, `values()`, `items()`
- Iteración sobre diccionarios

### 3. `tuplas_y_sets_completo.py`
Ejemplos de **TUPLAS** y **SETS** que incluyen:

**Tuplas:**
- Crear tuplas con `()`
- Acceso por índices (inmutables)
- Características: ordenadas, inmutables, permiten duplicados

**Sets:**
- Crear sets con `{}`
- Agregar/quitar elementos: `add()`, `remove()`, `discard()`
- Operaciones de conjuntos: unión `|`, intersección `&`, diferencia `-`
- Características: no ordenados, mutables, NO permiten duplicados

## Cómo ejecutar:

```bash
python3 listas_completo.py
python3 diccionario_completo.py
python3 tuplas_y_sets_completo.py
```

## Resumen de Estructuras de Datos:

| Tipo | Sintaxis | Ordenado | Mutable | Duplicados | Acceso |
|------|----------|----------|---------|------------|--------|
| Lista | `[a, b, c]` | ✅ | ✅ | ✅ | Índice |
| Diccionario | `{k: v}` | ✅* | ✅ | ✅ (valores) | Clave |
| Tupla | `(a, b, c)` | ✅ | ❌ | ✅ | Índice |
| Set | `{a, b, c}` | ❌ | ✅ | ❌ | - |

*A partir de Python 3.7+, los diccionarios mantienen el orden de inserción.