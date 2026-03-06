# Ejercicio 1

'''Determine si un número ingresado por el usuario es par o impar.'''

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Verificar si es par o impar
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")