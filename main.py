
from random import randint


def pedir_numero():
    """Solicita un número entre 1 y 100 y controla las entradas incorrectas."""
    while True:
        try:
            numero = int(input("Introduce un número entre 1 y 100: "))

            if 1 <= numero <= 100:
                return numero
            else:
                print("El número debe estar entre 1 y 100.")

        except ValueError:
            print("Error: debes introducir un número entero.")


def jugar_partida():
    """Realiza una partida con un máximo de diez intentos."""
    numero_secreto = randint(1, 100)
    intentos = 0
    ganado = False

    print("\nHe pensado un número entre 1 y 100. ¡Adivínalo!")

    while intentos < 10:
        numero = pedir_numero()
        intentos += 1

        if numero == numero_secreto:
            print("¡Correcto! Has acertado el número.")
            ganado = True
            break
        elif numero < numero_secreto:
            print("El número buscado es MAYOR.")
        else:
            print("El número buscado es MENOR.")

        print(f"Intentos restantes: {10 - intentos}")

    if not ganado:
        print(f"Has perdido. El número era {numero_secreto}.")

    print(f"Intentos utilizados: {intentos}")

    return ganado, intentos


def preguntar_repetir():
    """Pregunta al usuario si quiere comenzar otra partida."""
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Respuesta no válida. Introduce s o n.")


def main():
    """Controla las partidas y lleva el registro de victorias."""
    partidas = 0
    victorias = 0

    while True:
        ganado, intentos = jugar_partida()

        partidas += 1

        if ganado:
            victorias += 1

        print("\n----- ESTADÍSTICAS -----")
        print(f"Partidas jugadas: {partidas}")
        print(f"Partidas ganadas: {victorias}")

        if not preguntar_repetir():
            break

    print("\nGracias por jugar.")
    print(f"Total de partidas: {partidas}")
    print(f"Total de victorias: {victorias}")


main()