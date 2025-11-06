# ✅ Módulo 10 – Diccionarios y Tuplas - COMPLETADO

## 📋 Resumen de Ejercicios Completados

### 🗂️ Diccionarios (`m9_diccionario_ej1.py`)

✅ **TAREA 1: duplicados**
- Función que detecta elementos duplicados en secuencias (listas o cadenas)
- Implementación optimizada usando sets: `return len(seq) != len(set(seq))`

✅ **TAREA 2: encontrar_repeticiones** 
- Encuentra claves con valores > 1 en diccionarios
- Maneja tanto diccionarios como cadenas como parámetros

✅ **TAREA 3: suma_counters**
- Combina dos diccionarios sumando valores de claves comunes
- Implementación elegante usando `dict.get()` method

✅ **FUNCIÓN: is_interlocking**
- Verifica si una palabra se puede dividir en dos palabras válidas usando letras alternas
- Usa slicing `word[::2]` y `word[1::2]`

✅ **FUNCIÓN DE APOYO: contar_valores**
- Cuenta frecuencia de cada letra en una palabra
- Retorna diccionario {letra: cantidad}

### 🔗 Tuplas (`m9_tuplas_ej2.py`)

✅ **EJERCICIO 1: Tuplas no hashables**
- Demuestra que tuplas con elementos mutables no pueden ser claves de diccionario
- Manejo de excepciones con try-except

✅ **EJERCICIO 2: Cifrado César**
- Implementa cifrado César con desplazamiento circular
- Maneja caracteres especiales y acentos
- Usa mapeos de letras y aritmética modular

✅ **EJERCICIO 3: Letras más frecuentes**
- Cuenta y ordena letras por frecuencia (mayor a menor)
- Ignora espacios en el conteo

✅ **EJERCICIO 4: Anagramas en lista**
- Agrupa palabras que son anagramas
- Usa ordenamiento de letras como clave de agrupación

✅ **EJERCICIO 5: Distancia entre palabras**
- Calcula diferencias letra por letra entre palabras
- Usa `zip()` para comparación eficiente

✅ **EJERCICIO 6: Pares de metátesis**
- Encuentra pares de anagramas que difieren solo por intercambio de dos letras
- Combina lógica de anagramas con distancia de palabras

## 🧪 Pruebas Realizadas

Todos los ejercicios han sido probados y funcionan correctamente:

### Salida de Diccionarios:
```
--- Pruebas de has_duplicates ---
False
True
False
True

--- Pruebas de encontrar_repeticiones ---
{'b': 1, 'a': 3, 'n': 2}
['a', 'n']
['a', 'n']

--- Pruebas de suma_counters ---
{'b': 1, 'r': 3, 'o': 5, 'n': 1, 't': 2, 's': 4, 'a': 4, 'u': 2, 'i': 2, 'p': 1}

--- Pruebas de is_interlocking ---
False
False
```

### Salida de Tuplas:
```
EJERCICIO 1: Tupla no hashable
Tupla después de modificar: ([1, 2, 3], [4, 5, 6])
Error: No se puede usar la tupla como clave porque contiene elementos mutables (listas)

EJERCICIO 2: Cifrado César
hslnyph
íuéúó

EJERCICIO 3: Letras más frecuentes
[Listado completo de letras ordenadas por frecuencia]

EJERCICIO 4: Anagramas en lista
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

EJERCICIO 5: Distancia entre palabras
1
2

EJERCICIO 6: Pares de metátesis
(conserve, converse)
```

## 📝 Instrucciones para Entrega

1. ✅ Los archivos están listos en tu repositorio `/M9/`
2. 🔄 Ejecuta `git add .` para añadir los cambios
3. 📤 Ejecuta `git commit -m "Completado Módulo 10 - Diccionarios y Tuplas"`
4. 🚀 Ejecuta `git push origin main` para subir a GitHub
5. 🔗 Entrega el enlace del repositorio en Canvas

## 🎯 Conceptos Aprendidos

- **Diccionarios**: Manejo de claves y valores, conteo, combinación
- **Tuplas**: Inmutabilidad, acceso a elementos, uso como claves
- **Sets**: Detección de duplicados, operaciones de conjunto
- **List comprehensions**: Filtrado y transformación de datos
- **Manejo de excepciones**: try-except para errores previsibles
- **Algoritmos**: Cifrado César, análisis de anagramas, metátesis
- **Slicing**: Acceso a subsecuencias con `[::2]` y `[1::2]`

---
**Fecha de Completación**: Noviembre 5, 2025  
**Estado**: ✅ COMPLETADO Y LISTO PARA ENTREGA