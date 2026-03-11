CB = 2.8
FH = 1.18
FT = 0.88
RL = 1500

cons = 0

def calc_cons(dist, viento):
    global cons
    
    cons = dist * CB

    if viento == "headwind":
        cons = cons * FH
    elif viento == "tailwind":
        cons = cons * FT


comb = float(input("Ingrese combustible inicial (kg): "))

tr = 1
exito = True

while tr <= 5:

    print("--- Tramo", tr, "---")

    dist = float(input("Distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind / tailwind / cruzado): ")

    calc_cons(dist, viento)

    comb_proy = comb - cons

    if comb_proy <= RL:
        print("ALERTA CRITICA")
        print("Combustible insuficiente para continuar")
        print("Dirigirse al aeropuerto alterno")
        exito = False
        break

    comb = comb - cons

    print("Consumo del tramo:", round(cons, 2), "kg")
    print("Combustible restante:", round(comb, 2), "kg")

    tr = tr + 1


if exito:
    print("El vuelo fue exitoso y llego al destino.")
else:
    print("El vuelo fue abortado por seguridad.")

#en ia se investigo como poder modificar una variable que estuviera fuera de la función y nos arrojo que usáramos global+