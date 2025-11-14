## Entrega
El archivo Python gestion_registros.py (que debe contener la solución a ambas partes).
Los archivos de datos generados: mi_registro.txt y producto_nuevo.json.

# Parte 1: Seguir las instrucciones en gestion_registros.py

# Parte 2: El Conversor de Datos (CSV y JSON)

A. Instrucciones:
1. Usar el documento informacion.csv
2. El contenido debe ser el siguiente:

cantante, cancion, año, pais, nombre
Luis Fonsi, Despacito, 2017, Puerto Rico, Luis Alfonso Rodríguez López-Cepero
Shakira, La Tortura, 2005, Colombia, Shakira Isabel Mebarak Ripoll

B. Leer el CSV e Imprimir:

1. En gestion_registros.py, importa el módulo csv al inicio. 
2. Usa la estructura with open(...) junto con csv.reader() para leerlo.
3. Itera sobre las filas del documento e imprimir solo los cantantes.

Salida esperada:







C. Convertir un diccionario a JSON

1. En gestion_registors.py al inicio importar json.
2. Crea un diccionario llamado nuevo_producto asi:

nuevo_producto = {
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}

3. Usa la funcion json.dump() para guardar el diccionario en un nuevo archivo llamado producto_nuevo.json.

D. Cargar desde JSON (Deserialización):

1. Usa la función json.load() para abrir y leer producto_nuevo.json 
2. Guarda el resultado en un variable llamada data_cargada.
3. Imprime el Nombre y el Precio del producto cargado para verificar que fue exitosa.

Salida esperada:
Producto cargado desde JSON:
Nombre: Webcam
Precio: 45.99
