#Generar una constante de texto que será la contraseña. luego pida al usuario que ingrese la contraseña. mientras la contraseña no sea la correcta, dembe de continuar a pedri la contraseña. siesta esta correcta, se deja continuar al resto del programa

pas = "Asoris"

clave = input("Ingrese la contraseña: ")

while clave != pas:

    print("Contraseña incorrecta. Intente nuevamente.")
    clave = input("Ingrese la contraseña: ")

print("Contraseña correcta.")


