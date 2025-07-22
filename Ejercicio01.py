print("Simulador de votación con validación cruzada")
nombre = input("Nombre completo: ")
dpi = input("DPI: ")
departamento = input("Departamento: ").lower()
anoNacimiento = int(input("Año de nacimiento: "))

if len(nombre) < 5:
    print("El nombre es demasiado corto, intente con otro nombre.")
elif len(dpi) != 13:
    print("DPI inválido debe tener 13 dígitos")
else:
    edad = 2025 - anoNacimiento

    if edad >= 18:
        print(f"Bienvenido {nombre}, su centro de votacion esta en {departamento}")
    elif edad == 17 and (departamento == "peten" or departamento == "alta verapaz"):
        print(f"Bienvenido {nombre}, su centro de votacion está en {departamento}")
    else:
        print("No puede votar aun no cuenta con la edad suficiente")