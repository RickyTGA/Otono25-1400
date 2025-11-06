# TODO 1: Crear la clase Time y asignar atributos

Objetivo: Crear la clase Time que represente un momento en el día con los atributos hour, minute y second.

Instrucciones:

Define la clase Time.

Implementa el método __init__() para inicializar los atributos hour, minute, y second con valores por defecto (puedes usar 0 como valor inicial).

Crea un objeto Time llamado mi_hora y asigna valores a los atributos: hour = 14, minute = 30, second = 15.

Resultado esperado:

Un objeto de la clase Time con los valores inicializados correctamente.

# TODO 2: Crear una función para sumar horas, minutos y segundos

Objetivo: Escribir una función que reciba un objeto Time y una duración en horas, minutos y segundos, y devuelva un nuevo objeto Time con el resultado de la suma.

Instrucciones:

Crea una función llamada add_time() que reciba un objeto Time y tres parámetros: horas, minutos y segundos.

La función debe devolver un nuevo objeto Time que sea el resultado de sumar la duración al objeto original.

Para esto, usa la función time_to_int() y int_to_time() (de conversión entre formato de tiempo y segundos).

Resultado esperado:

Un objeto Time con el tiempo actualizado después de sumar la duración proporcionada.

# TODO 3: Modificar la clase Time para hacerla más robusta

Objetivo: Mejorar la clase Time añadiendo métodos para mostrar la hora correctamente con formato de dos dígitos, y para manejar casos en los que los minutos o segundos superan el valor de 60.

Instrucciones:

Modifica la clase Time para agregar un método llamado __str__() que devuelva una cadena con el formato adecuado: hh:mm:ss, con ceros a la izquierda si es necesario.

También, actualiza la función increment_time() para que si el valor de los minutos o segundos supera 60, se ajuste correctamente.

Resultado esperado:

Al imprimir un objeto Time, se debe mostrar correctamente con el formato hh:mm:ss.

La función increment_time() debe ser capaz de manejar incrementos que superen los 60 minutos o segundos.