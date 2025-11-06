# Programa para gestionar las notas de los estudiantes

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Salir")

def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return None
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            notas = []
            for i in range(3):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)

            promedio = calcular_promedio(notas)
            aprobado = promedio >= 6.0
            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }
            estudiantes.append(estudiante)
            print(f"\nEstudiante {nombre} agregado correctamente.")

        elif opcion == "2":
            print("\n=== LISTA DE ESTUDIANTES ===")
            for est in estudiantes:
                estado = "Aprobado" if est["aprobado"] else "Reprobado"
                print(f"{est['nombre']} - Promedio: {est['promedio']:.2f} - {estado}")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

main()

https://github.com/RickyTGA/Otono25-1400
