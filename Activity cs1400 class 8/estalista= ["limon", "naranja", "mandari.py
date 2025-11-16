estalista = ["limon", "naranja", "mandarina", "fresa", "kiwi"]
print(estalista)

estalista.append("mango")
estalista.append("piña")
print("estalista después de agregar mango y piña")
print(estalista)

colores = ["rojo", "verde", "azul"]
mezcladas = [*colores, *estalista]
print("Lista mezclada:", mezcladas)