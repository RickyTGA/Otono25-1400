#TODO #1 y #3
class Tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
    def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24

    # ahora ajusta el tiempo si excede
    def incrementar_tiempo(self, horas, minutos, segundos):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self


#TODO #2 
#convirtiendo tiempo original a los segundos
#convertir el total de segundos a un objeto Tiempo
    
def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos
    
def int_a_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return Tiempo(horas, minutos, segundos)
    
def sumar_tiempo(tiempo, horas, minutos, segundos):
    total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
    return int_a_tiempo(total_segundos)


mi_hora = Tiempo(14, 30, 15)
print("Hora inicial:", mi_hora)


#TODO #3
nueva_hora = sumar_tiempo(mi_hora, 2, 50, 30)
print("Nueva Hora:", nueva_hora)

mi_hora.incrementar_tiempo(1, 45, 30)
print("Hora incrementada:", mi_hora)

tiempo_desbordado = sumar_tiempo(mi_hora, 0, 120, 3600)
print("Hora después del overflow:", tiempo_desbordado)
