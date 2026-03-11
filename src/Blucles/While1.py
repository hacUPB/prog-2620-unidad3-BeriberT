#solicitar dos númeron al usuario e implementar los avlores pares que hay entre dicho números.

# Solicitar dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Asegurar que el primer número sea el menor
if num1 > num2:
    num1, num2 = num2, num1

i= num1

while i <= num2:
    if i % 2 == 0:
        print(i)
    i = i + 1

    