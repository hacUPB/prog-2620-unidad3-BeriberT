#1. calcular el valor de la propina, el total a pagar y el valor individual a pagar por cada invitado, dado el valor de la cuenta y el número de invitados.

from ast import Or


cuenta = 85

Invitados = 4

Propina = (cuenta * 0.15)

total = cuenta+ Propina

print ("El valor de la propina es: " + str(Propina))

print ("El valor total a pagar es: " + str(total))

print ("El valor individual a pagar es: " + str(total/Invitados))


#2.# Altura mínima requerida para la montaña rusa en cm

altura_minima = 150

# Altura del visitante en cm
altura_visitante = input("Ingrese la altura del visitante en cm: ")

## Usamos un operador relacional para verificar si el visitante puede subir
puede_subir = int(altura_visitante) >= altura_minima
No_puede_subir = int(altura_visitante) < altura_minima
## Imprimimos el resultado

print(f"El visitante puede subir a la montaña rusa: {puede_subir}") 
print(f"El visitante no puede subir a la montaña rusa: {No_puede_subir}")

#

# 4 Reto Final: El Validador de Videojuegos

# Datos del usuario
edad_usuario = 18
saldo_billetera = 55.0
tiene_suscripcion_premium = True

# Precio base del juego
precio_juego = 60

# Cálculo del descuento (10% si es premium)
descuento = precio_juego * 0.10 * tiene_suscripcion_premium

# Precio final
precio_final = precio_juego - descuento

# Evaluación de condiciones
cumple_edad = edad_usuario >= 17
tiene_saldo = saldo_billetera >= precio_final

# Resultado final
compra_exitosa = cumple_edad and tiene_saldo

# Resultados
print("Precio final del juego:", precio_final)
print("¿Cumple la edad mínima?:", cumple_edad)
print("¿Tiene saldo suficiente?:", tiene_saldo)
print("¿La compra es exitosa?:", compra_exitosa)