
import random
import string

repetir = 1

while repetir == 1:

# Menú principal
    print("\n========================")
    print("GENERADOR DE CONTRASEÑAS")
    print("========================")
    print("1. Generar contraseña")
    print("2. Salir")

    opcion = int(input("Ingrese una opción (1 o 2): "))

    while opcion != 1 and opcion != 2:
        print("Opción no válida.")
        opcion = int(input("Ingrese una opción (1 o 2): "))

# Solicitar configuración de la contraseña
    if opcion == 1:

        longitud = int(input("Ingrese la longitud de la contraseña: "))

        while longitud < 4:
            print("Error: la longitud mínima es 4.")
            longitud = int(input("Ingrese nuevamente la longitud: "))

        mayusculas = int(input("¿Incluir mayúsculas? (1=Sí, 2=No): "))

        while mayusculas != 1 and mayusculas != 2:
            print("Opción no válida.")
            mayusculas = int(input("¿Incluir mayúsculas? (1=Sí, 2=No): "))

        minusculas = int(input("¿Incluir minúsculas? (1=Sí, 2=No): "))

        while minusculas != 1 and minusculas != 2:
            print("Opción no válida.")
            minusculas = int(input("¿Incluir minúsculas? (1=Sí, 2=No): "))

        numeros = int(input("¿Incluir números? (1=Sí, 2=No): "))

        while numeros != 1 and numeros != 2:
            print("Opción no válida.")
            numeros = int(input("¿Incluir números? (1=Sí, 2=No): "))

        simbolos = int(input("¿Incluir símbolos? (1=Sí, 2=No): "))

        while simbolos != 1 and simbolos != 2:
            print("Opción no válida.")
            simbolos = int(input("¿Incluir símbolos? (1=Sí, 2=No): "))

# Construir el conjunto de caracteres permitidos
        caracteres = ""

        if mayusculas == 1:
            caracteres = caracteres + string.ascii_uppercase

        if minusculas == 1:
            caracteres = caracteres + string.ascii_lowercase

        if numeros == 1:
            caracteres = caracteres + string.digits

        if simbolos == 1:
            caracteres = caracteres + "!@#$%&*?"

        if caracteres == "":
            print("Error: Debe seleccionar al menos una opción.")
        
        else:

            # Crear la contraseña garantizando al menos un carácter
            # de cada tipo seleccionado

            contraseña = []

            if mayusculas == 1:
                contraseña.append(random.choice(string.ascii_uppercase))

            if minusculas == 1:
                contraseña.append(random.choice(string.ascii_lowercase))

            if numeros == 1:
                contraseña.append(random.choice(string.digits))

            if simbolos == 1:
                contraseña.append(random.choice("!@#$%&*?"))

            # Completar la longitud restante
            while len(contraseña) < longitud:
                contraseña.append(random.choice(caracteres))

            # Mezclar los caracteres para que no queden siempre al inicio
            random.shuffle(contraseña)

            contraseña = "".join(contraseña)

            print("\nGenerando contraseña...")
            print("Contraseña generada correctamente.")
            print("Contraseña:", contraseña)

        print("\n¿Desea generar otra contraseña?")
        print("1 = Sí")
        print("2 = No")

        repetir = int(input("Ingrese una opción: "))

        while repetir != 1 and repetir != 2:
            print("Opción no válida.")
            repetir = int(input("Ingrese una opción (1 o 2): "))

    else:
        repetir = 2


    print("\nPrograma finalizado.")
