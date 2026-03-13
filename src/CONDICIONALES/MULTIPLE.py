
# Ejercicio 2

'''El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

- Infancia (0-6 años)
- Niñez (6 - 12 años)
- Adolescencia (12 - 20 años)
- Juventud (20 - 25 años)
- Adultez (25- 60 años)
- Ancianidad / Vejez (60 años o más)'''

# Solicitar la edad
edad = int(input("Ingrese su edad: "))

# Validar que no sea negativa
if edad < 0:
    print("Error: La edad no puede ser menor que cero.")
else:
    match edad:
        case edad if 0 <= edad <= 6:
            print("Etapa: Infancia")
        case edad if 7 <= edad <= 12:
            print("Etapa: Niñez")
        case edad if 13 <= edad <= 20:
            print("Etapa: Adolescencia")
        case edad if 21 <= edad <= 25:
            print("Etapa: Juventud")
        case edad if 26 <= edad <= 60:
            print("Etapa: Adultez")
        case _:
            print("Etapa: Ancianidad / Vejez")

