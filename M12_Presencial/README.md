## Entrega
El archivo Python gestion_registros.py (que debe contener la solución a ambas partes).
Los archivos de datos generados: mi_registro.txt y producto_nuevo.json.

# Parte 1: Seguir las instrucciones en gestion_registros.py

# Parte 2: El Conversor de Datos (CSV y JSON)

A. Instrucciones:
1. Crear un documento y llamarlo inventario.csv
2. Puedes crearlo manualmente (editor de texto o excel) o automaticamente usando Python.
3. El contenido debe ser el siguiente:

ID,Nombre,Precio,Stock
101,Monitor,150.99,25
102,Teclado,35.50,150
103,Raton,18.00,300

B. Leer el CSV e Imprimir:

1. En gestion_registros.py, importa el módulo csv al inicio. 
2. Usa la estructura with open(...) junto con csv.reader() para leer inventario.py.
3. Itera sobre las filas del documento e imprimi solo los productos cuyo stock sea menor a 100. 

Salida esperada:
Productos con bajo stock:
ID: 101, Nombre: Monitor, Stock: 25

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
