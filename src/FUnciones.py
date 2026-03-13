# # crear una función que calcule el factorial de un número y lo retone


# def factorial(numero):
#     # si numero es 0 facorial es 1
#     # si numero es menor que 0 retornar "no se puede calcular el factorial"
#     # multiplicar desde 1 hasta nuemro y acumular 
#     acumulador = 1 
#     if numero < 0:
#         return -1
#     for factor in range(1,numero+1):
#         acumulador = acumulador * factor
#         #acumuladro *= factor       
#     return acumulador

# resultado = factorial(-7)
# print(resultado)

# funcion de menu

# def menu():
#         print("1. suma\n 2. resta \n 3. Multiplicación\n 4. divición")
#         opcion = (input("selecione una opción: "))
#         return opcion

# operacion = menu()
# print (f"El usuario eligio la opción: {operacion}")


# import hashlib
# import unicodedata
# import random
# import string

# def normalizar(txt):
#     txt = txt.lower()
#     txt = ''.join(
#         c for c in unicodedata.normalize('NFD', txt)
#         if unicodedata.category(c) != 'Mn'
#     )
#     return txt.strip()

# claves = [
# "Bala la la la",
# "Luna",
# "Chocolate🍫",
# "Entregó todo entero",
# "Para mí es otro día",
# "Del siglo xxi",
# "Hola",
# "Parte de tu mundo",
# "Denna",
# "Trucha"
# ]

# salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

# print("SALT =", salt)
# print()

# for c in claves:
#     n = normalizar(c)
#     h = hashlib.sha256((salt+n).encode()).hexdigest()
#     print(h)

