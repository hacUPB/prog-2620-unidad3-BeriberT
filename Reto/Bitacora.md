**Datos de entrada**
|nombre|descripcion|
|------|-----------|
|combustible actual|combustible inicial del vuelo|
|distancia|distancia del tramo|
|viento|tipo de viento|
||

**Datos de salida**
|nombre|descripcion|
|------|-----------|
|consumo|consumo del tramo|
|combustible_actual|combustible restante|
|ALERTA CRITICA|	Mensaje de combustible insuficiente para continuar el vuelo|
|Combustible insuficiente para continuar|mensaje que informa que el combustible proyectado está por debajo de la reserva legal|
|Se debe aterrizar en el aeropuerto alterno|muestra una advertencia al piloto para realizar un aterrizaje en un aeropuerto alterno|
|El vuelo fue exitoso. Se llego al destino con combustible seguro|myestra al piloto que el vuelo terminó correctamente|
|El vuelo fue abortado por seguridad|muestra al piloto que el vuelo se debe cancelar por insuficiencia de combustible|
||

**Tabla de constantes**
|nombre|descripcion|valor|
|-|-|-|
|CONSUMO_BASE|consumo del combustible|2.8|
|FACTOR_HEADWIND|factor de aumento de consumo por viento en contra|1.18|
|FACTOR_TAILWIND|factor de reduccion de consumo por viento a favor|0.88|
|RESERVA_LEGAL|reserva minima de combustible que debe llevar el avion|1500|
||

**Tabla de vriables**
|nombre|descripcion|
|------|-----------|
|combustible actual|combustible inicial del vuelo|
|distancia|distancia del tramo|
|viento|tipo de viento|
|combustible_proyectado|combustible estimado despues de cada tramo del vuelo|
|consumo|combustible que se consume en cada tramo|
|vuelo_exitoso|informa si el vuelo finalizo con normalidad o se aborto por seguridad|
||

.

.

.

```
inicio

CONSUMO_BASE = 2.8                                                                                             
FACTOR_HEADWIND = 1.18
FACTOR_TAILWIND = 0.88
RESERVA_LEGAL = 1500

Escribir "Ingrese combustible inicial (kg): "
Leer combustible_actual

vuelo_exitoso = Verdadero

Para tramo = 1 Hasta 5 Hacer

    Escribir "--- Tramo ", tramo, " ---"

    Escribir "Distancia del tramo (km): "
    Leer distancia

    Escribir "Tipo de viento (headwind / tailwind / cruzado): "
    Leer viento

    consumo = distancia * CONSUMO_BASE

    Si viento = "headwind" Entonces
        consumo <- consumo * FACTOR_HEADWIND
    Sino
        Si viento = "tailwind" Entonces
            consumo = consumo * FACTOR_TAILWIND
        FinSi
    FinSi

    combustible_proyectado = combustible_actual - consumo

    Si combustible_proyectado <= RESERVA_LEGAL Entonces
       Escribir "ALERTA CRITICA"
       Escribir "Combustible insuficiente para continuar."
       Escribir "Se debe aterrizar en el aeropuerto alterno."

    vuelo_exitoso <- Falso
    Salir
    FinSi

    combustible_actual = combustible_actual - consumo

    Escribir "Consumo del tramo: ", consumo
    Escribir "Combustible restante: ", combustible_actual

FinPara

Si vuelo_exitoso = Verdadero Entonces
    Escribir "El vuelo fue exitoso. Se llego al destino con combustible seguro."
Sino
    Escribir "El vuelo fue abortado por seguridad."
FinSi

Fin
```