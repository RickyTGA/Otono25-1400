# Crear una tupla
estatupla = ("limon", "naranja", "mandarina", "manzana", "uva")

# Imprimir la tupla completa
print("Tupla completa:")
print(estatupla)

# Imprimir la longitud de la tupla
print(f"\nLa tupla tiene {len(estatupla)} elementos")

# Acceder a elementos de la tupla (como en las listas)
print("\n--- Accediendo a elementos de la tupla ---")
print(f"Primer elemento: {estatupla[0]}")
print(f"Último elemento: {estatupla[-1]}")
print(f"Elementos del índice 1 al 3: {estatupla[1:3]}")

# Las tuplas son inmutables (no se pueden modificar)
print("\n--- Características de las tuplas ---")
print("Las tuplas son INMUTABLES - no se pueden modificar después de crearlas")

# Iterar sobre la tupla
print("\n--- Iterando sobre la tupla ---")
for i, fruta in enumerate(estatupla):
    print(f"Posición {i}: {fruta}")

# Crear un set
esteset = {"limon", "naranja", "mandarina", "manzana", "uva", "limon", "naranja"}

print("\n" + "="*50)
print("SETS (CONJUNTOS)")
print("="*50)

# Imprimir el set completo
print("\nSet completo:")
print(esteset)
print("Nota: Los sets eliminan automáticamente los elementos duplicados")

# Imprimir la longitud del set
print(f"\nEl set tiene {len(esteset)} elementos únicos")

# Agregar elementos al set
print("\n--- Agregando elementos al set ---")
esteset.add("platano")
esteset.add("fresa")
print(f"Después de agregar elementos: {esteset}")

# Intentar agregar un elemento duplicado
esteset.add("limon")  # No se agregará porque ya existe
print(f"Después de intentar agregar 'limon' duplicado: {esteset}")

# Quitar elementos del set
print("\n--- Quitando elementos del set ---")
esteset.remove("mandarina")
print(f"Después de quitar 'mandarina': {esteset}")

# Usar discard (no da error si el elemento no existe)
esteset.discard("kiwi")  # No existe, pero no da error
print(f"Después de usar discard con elemento inexistente: {esteset}")

# Operaciones de conjuntos
print("\n--- Operaciones de conjuntos ---")
set1 = {"manzana", "pera", "uva"}
set2 = {"uva", "platano", "fresa"}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Unión (|): {set1 | set2}")
print(f"Intersección (&): {set1 & set2}")
print(f"Diferencia (-): {set1 - set2}")

# Iterar sobre el set
print("\n--- Iterando sobre el set ---")
for fruta in esteset:
    print(f"Fruta en el set: {fruta}")

# Convertir entre tipos
print("\n--- Conversiones ---")
tupla_desde_set = tuple(esteset)
lista_desde_tupla = list(estatupla)
set_desde_lista = set(lista_desde_tupla)

print(f"Tupla convertida desde set: {tupla_desde_set}")
print(f"Lista convertida desde tupla: {lista_desde_tupla}")
print(f"Set convertido desde lista: {set_desde_lista}")

# Resumen final
print(f"\n--- Resumen final ---")
print(f"Tupla original: {estatupla} (longitud: {len(estatupla)})")
print(f"Set final: {esteset} (longitud: {len(esteset)})")
print("\nCaracterísticas:")
print("- Tupla: Ordenada, inmutable, permite duplicados")
print("- Set: No ordenado, mutable, NO permite duplicados")