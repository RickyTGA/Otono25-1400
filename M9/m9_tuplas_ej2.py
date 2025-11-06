"""
PROYECTO DE PROGRAMACIÓN: Cadenas, tuplas, diccionarios y anagramas

Instrucciones:
Lee con atención cada ejercicio. Completa el código en las secciones marcadas como TODO.
Puedes probar tus funciones en la sección "if __name__ == '__main__'".
"""

# ============================
# EJERCICIO 1: Tuplas no hashables
# ============================

def tupla_no_hashable():
    """
    Crea una tupla que contiene listas como elementos. Intenta usarla como clave en un diccionario.
    """
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # TODO: Añade el número 6 al final de la segunda lista (list1) usando t
    # Resultado esperado: ([1, 2, 3], [4, 5, 6])
    t[1].append(6)  # Accedemos a list1 a través de la tupla y añadimos 6
    print(f"Tupla después de modificar: {t}")

    # TODO: Intenta usar la tupla t como clave en un diccionario y captura el error con try-except
    # Debes imprimir un mensaje que diga que no se puede usar como clave si ocurre un TypeError
    try:
        diccionario = {t: "valor"}
        print("La tupla se pudo usar como clave")
    except TypeError:
        print("Error: No se puede usar la tupla como clave porque contiene elementos mutables (listas)")


# ============================
# EJERCICIO 2: Cifrado César
# ============================

def shift_word(word, shift):
    """
    Aplica un cifrado César a la palabra dada, desplazando cada letra por 'shift' posiciones.
    Se espera que la palabra esté en minúsculas y sin caracteres especiales.

    Ejemplo:
    shift_word("alegria", 7) -> "alegre"
    shift_word("melon", 16) -> "al cubo"
    """
    # TODO: Implementa el cifrado César aquí
    # Tip: Usa letter_map y operador % para hacer el desplazamiento circular
    letters = 'abcdefghijklmnopqrstuvwxyzáéíóúñ '
    letter_map = dict(zip(letters, range(len(letters))))
    reverse_map = dict(zip(range(len(letters)), letters))
    result = []

    # Recorre cada letra y aplícale el desplazamiento
    for letter in word:
        # TODO: Maneja letras no reconocidas (espacios, tildes, etc.)
        if letter in letter_map:
            # Obtenemos la posición actual de la letra
            old_position = letter_map[letter]
            # Calculamos la nueva posición con desplazamiento circular
            new_position = (old_position + shift) % len(letters)
            # Obtenemos la nueva letra
            new_letter = reverse_map[new_position]
            result.append(new_letter)
        else:
            # Si la letra no está en nuestro mapeo, la dejamos como está
            result.append(letter)

    # Une la lista resultante en una cadena
    return ''.join(result)


# ============================
# EJERCICIO 3: Letras más frecuentes
# ============================

def most_frequent_letters(texto):
    """
    Recibe una cadena y muestra las letras ordenadas por frecuencia (de mayor a menor).
    """
    # TODO: Cuenta las letras ignorando espacios y ordena por frecuencia
    # Tip: Usa value_counts() del ejercicio anterior si lo tienes
    contador = {}
    
    # Contamos las letras, ignorando espacios
    for letra in texto.lower():
        if letra != ' ':  # Ignoramos espacios
            contador[letra] = contador.get(letra, 0) + 1
    
    # Ordenamos por frecuencia (de mayor a menor)
    letras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Mostramos los resultados
    print("Letras ordenadas por frecuencia:")
    for letra, frecuencia in letras_ordenadas:
        print(f"'{letra}': {frecuencia}")
    
    return letras_ordenadas


# ============================
# EJERCICIO 4: Anagramas en lista
# ============================

def encontrar_anagramas(lista_palabras):
    """
    Dada una lista de palabras, imprime todos los grupos de palabras que son anagramas.

    Ejemplo de salida:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    """
    # TODO: Crea un diccionario que relacione la palabra ordenada con sus anagramas
    grupos_anagramas = {}
    
    for palabra in lista_palabras:
        # Ordenamos las letras de la palabra para crear una clave
        clave = ''.join(sorted(palabra))
        
        # Añadimos la palabra al grupo correspondiente
        if clave in grupos_anagramas:
            grupos_anagramas[clave].append(palabra)
        else:
            grupos_anagramas[clave] = [palabra]
    
    # Imprimimos solo los grupos que tienen más de una palabra (anagramas)
    for clave, grupo in grupos_anagramas.items():
        if len(grupo) > 1:
            print(grupo)


# ============================
# EJERCICIO 5: Distancia entre palabras
# ============================

def word_distance(word1, word2):
    """
    Devuelve el número de letras distintas entre dos palabras de igual longitud.

    Ejemplo:
    word_distance("casa", "cata") -> 1
    """
    # TODO: Usa zip para comparar letra por letra y contar diferencias
    if len(word1) != len(word2):
        return -1  # Retornamos -1 si las palabras no tienen la misma longitud
    
    diferencias = 0
    for letra1, letra2 in zip(word1, word2):
        if letra1 != letra2:
            diferencias += 1
    
    return diferencias


# ============================
# EJERCICIO 6: Pares de metátesis
# ============================

def encontrar_metatesis(lista_palabras):
    """
    Imprime todos los pares de palabras que son anagramas y difieren solo por una transposición (intercambio de dos letras).

    Ejemplo:
    ('converse', 'conserve')
    """
    # TODO:
    # 1. Encuentra anagramas usando el mismo enfoque del ejercicio anterior
    # 2. Para cada par en cada grupo de anagramas, verifica si son pares de metátesis
    #    (solo deben diferir en exactamente dos letras y ser del mismo largo)
    
    grupos_anagramas = {}
    
    # Agrupamos anagramas
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        if clave in grupos_anagramas:
            grupos_anagramas[clave].append(palabra)
        else:
            grupos_anagramas[clave] = [palabra]
    
    # Verificamos pares de metátesis en cada grupo de anagramas
    for grupo in grupos_anagramas.values():
        if len(grupo) > 1:
            # Comparamos cada par de palabras en el grupo
            for i in range(len(grupo)):
                for j in range(i + 1, len(grupo)):
                    word1, word2 = grupo[i], grupo[j]
                    # Verificamos si difieren en exactamente 2 posiciones
                    if word_distance(word1, word2) == 2:
                        print(f"({word1}, {word2})")


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    print("EJERCICIO 1: Tupla no hashable")
    tupla_no_hashable()

    print("\nEJERCICIO 2: Cifrado César")
    print(shift_word("alegria", 7))    # Esperado: "alegre"
    print(shift_word("melon", 16))     # Esperado: "al cubo"

    print("\nEJERCICIO 3: Letras más frecuentes")
    most_frequent_letters("el veloz murciélago hindú comía feliz cardillo y kiwi")

    print("\nEJERCICIO 4: Anagramas en lista")
    palabras = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
    encontrar_anagramas(palabras)

    print("\nEJERCICIO 5: Distancia entre palabras")
    print(word_distance("casa", "cata"))  # Esperado: 1
    print(word_distance("luz", "pez"))    # Esperado: 2

    print("\nEJERCICIO 6: Pares de metátesis")
    palabras = ['conserve', 'converse', 'recostar', 'rescatro', 'resmelts', 'smelters', 'termless']
    encontrar_metatesis(palabras)
