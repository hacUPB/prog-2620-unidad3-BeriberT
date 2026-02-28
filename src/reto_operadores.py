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