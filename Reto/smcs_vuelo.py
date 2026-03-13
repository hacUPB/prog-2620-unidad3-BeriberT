# SMCS - Sistema de Monitoreo de Combustible

CONSUMO_BASE = 2.8
FACTOR_HEADWIND = 1.18
FACTOR_TAILWIND = 0.88
RESERVA_LEGAL = 1500


def calcular_consumo_tramo(distancia, viento):
    consumo = distancia * CONSUMO_BASE

    if viento == "headwind":
        consumo = consumo * FACTOR_HEADWIND

    elif viento == "tailwind":
        consumo = consumo * FACTOR_TAILWIND

    return consumo


combustible_actual = float(input("Ingrese combustible inicial (kg): "))

vuelo_exitoso = True

for tramo in range(1, 6):

    print("--- Tramo", tramo, "---")

    distancia = float(input("Distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind / tailwind / cruzado): ")

    consumo = calcular_consumo_tramo(distancia, viento)

    combustible_proyectado = combustible_actual - consumo

    if combustible_proyectado <= RESERVA_LEGAL:
        print("ALERTA CRITICA")
        print("Combustible insuficiente para continuar.")
        print("Se debe aterrizar en el aeropuerto alterno.")
        vuelo_exitoso = False
        break

    combustible_actual = combustible_actual - consumo

    print("Consumo del tramo:", round(consumo, 2), "kg")
    print("Combustible restante:", round(combustible_actual, 2), "kg")


if vuelo_exitoso:
    print("El vuelo fue exitoso. Se llego al destino con combustible seguro.")
else:
    print("El vuelo fue abortado por seguridad.")

