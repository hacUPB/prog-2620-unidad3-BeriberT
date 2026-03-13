# Ejercicio 1.

'''
Un almacén cobra $9 000 por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a $100 000. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
'''

# Solicitar el valor de la compra
compra = int(input("Ingrese el valor de la compra: "))

# Inicialmente se suma el costo de envío
total = compra + 9000

# Condicional simple
if compra > 100000:
    total = compra

# Mostrar el total a pagar
print("El valor total a pagar es: $", total)