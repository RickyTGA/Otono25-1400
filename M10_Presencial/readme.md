# TODO 1: Crear la clase Tiempo y asignar atributos

Objetivo: Crear la clase Time que represente un momento en el día con los atributos hora, minuto y segundo.

Instrucciones:

Define la clase Time.

Implementa el método __init__() para inicializar los atributos hour, minute, y second con valores por defecto (puedes usar 0 como valor inicial).

Crea un objeto Time llamado mi_hora y asigna valores a los atributos: hour = 14, minute = 30, second = 15.

Resultado esperado:

Un objeto de la clase Time con los valores inicializados correctamente.

# TODO 2: Crear funciónes afuera de la clase para sumar horas, minutos y segundos

Objetivo: Escribir una función que reciba un objeto Tiempo y una duración en horas, minutos y segundos, y devuelva un nuevo objeto Tiempo con el resultado de la suma.

Instrucciones:

Crea una función llamada sumar_tiempo() que reciba un objeto Tiempo y tres parámetros: horas, minutos y segundos.

La función debe devolver un nuevo objeto Tiempo que sea el resultado de sumar la duración al objeto original.

Para esto, usa la función tiempo_a_int() y int_a_tiempo() (de conversión entre formato de tiempo y segundos).

Resultado esperado:

Un objeto Time con el tiempo actualizado después de sumar la duración proporcionada.

# TODO 3: Modificar la clase Tiempo para hacerla más robusta

Objetivo: Mejorar la clase Time añadiendo métodos para mostrar la hora correctamente con formato de dos dígitos, y para manejar casos en los que los minutos o segundos superan el valor de 60.

Instrucciones:

Modifica la clase Tiempo para agregar un método llamado __str__() que devuelva una cadena con el formato adecuado: hh:mm:ss, con ceros a la izquierda si es necesario.
Modifica la clase Tiempo para agregar un método llamado _normalize()  para asegurar si los segundos o minutos exceden mas de 60, se pasen a un minuto o una hora completa.
También, actualiza la función incrementar_tiempo() para que si el valor de los minutos o segundos supera 60, se ajuste correctamente.


Resultado esperado:

Al imprimir un objeto Tiempo, se debe mostrar correctamente con el formato hh:mm:ss.

La función aumentar_tiempo() debe ser capaz de manejar incrementos que superen los 60 minutos o segundos.

Hora inicial: 14:30:15
Nueva hora: 17:20:00
Hora incrementada: 18:15:45
Hora después del overflow: 21:15:45
