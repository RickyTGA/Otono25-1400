# Crear una lista de items
lista_frutas = ["Manzana", "Limón", "Papaya", "Plátano", "Naranja"]

# Mostrar la lista
print("Lista de frutas:", lista_frutas)

# Usar len() para obtener la longitud de la lista
longitud = len(lista_frutas)
print(f"La lista tiene {longitud} elementos")

# Ejemplo adicional con diferentes tipos de items
lista_mixta = ["Python", 2024, True, 3.14, "Programación"]
print("\nLista mixta:", lista_mixta)
print(f"La lista mixta tiene {len(lista_mixta)} elementos")

# Ejemplo con lista vacía
lista_vacia = []
print(f"\nLa lista vacía tiene {len(lista_vacia)} elementos")

# Usar índice -1 para acceder al último elemento
print("\n--- Usando índice -1 ---")
print(f"El último elemento de la lista de frutas es: {lista_frutas[-1]}")
print(f"El penúltimo elemento es: {lista_frutas[-2]}")
print(f"El primer elemento usando índice positivo: {lista_frutas[0]}")
print(f"El primer elemento usando índice negativo: {lista_frutas[-len(lista_frutas)]}")

# Mostrar todos los índices negativos
print("\nTodos los elementos usando índices negativos:")
for i in range(1, len(lista_frutas) + 1):
    print(f"Índice -{i}: {lista_frutas[-i]}")

# Usar slicing [1:3] para obtener una porción de la lista
print("\n--- Usando slicing [1:3] ---")
porcion = lista_frutas[1:3]
print(f"Lista completa: {lista_frutas}")
print(f"Elementos del índice 1 al 2 (no incluye el 3): {porcion}")
print(f"Longitud de la porción: {len(porcion)}")

# Más ejemplos de slicing
print("\nMás ejemplos de slicing:")
print(f"Primeros 3 elementos [0:3]: {lista_frutas[0:3]}")
print(f"Últimos 2 elementos [-2:]: {lista_frutas[-2:]}")
print(f"Todos excepto el primero [1:]: {lista_frutas[1:]}")
print(f"Todos excepto el último [:-1]: {lista_frutas[:-1]}")
print(f"Del segundo al cuarto [1:4]: {lista_frutas[1:4]}")

# Agregar elementos a la lista
print("\n--- Agregando elementos a la lista ---")
print(f"Lista original: {lista_frutas}")

# Agregar un elemento al final
lista_frutas.append("Uva")
print(f"Después de agregar 'Uva': {lista_frutas}")

# Agregar un elemento en una posición específica
lista_frutas.insert(2, "Fresa")
print(f"Después de insertar 'Fresa' en posición 2: {lista_frutas}")

# Agregar múltiples elementos
lista_frutas.extend(["Kiwi", "Mango"])
print(f"Después de agregar múltiples elementos: {lista_frutas}")

# Quitar elementos de la lista
print("\n--- Quitando elementos de la lista ---")
print(f"Lista antes de quitar elementos: {lista_frutas}")

# Quitar un elemento específico por valor
lista_frutas.remove("Limón")
print(f"Después de quitar 'Limón': {lista_frutas}")

# Quitar un elemento por índice
elemento_quitado = lista_frutas.pop(1)
print(f"Después de quitar elemento en índice 1 ('{elemento_quitado}'): {lista_frutas}")

# Quitar el último elemento
ultimo_elemento = lista_frutas.pop()
print(f"Después de quitar el último elemento ('{ultimo_elemento}'): {lista_frutas}")

# Imprimir estado final
print(f"\n--- Estado final ---")
print(f"Lista final: {lista_frutas}")
print(f"Longitud final: {len(lista_frutas)} elementos")