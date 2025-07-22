print("Simulador de entradas al cine con validación múltiple")
edad = int(input("Dime tu edad: "))
dia = input("Indica el dia de la semana en la que estamos hoy: ").lower()
estudiante = input("Eres estudiante? (sí/no): ").lower()

if edad < 13:
    print("No puedes ver esta película. Es para mayores de 15 años.")
else:
    if estudiante == "si":
        precio = 35
    else:
        precio = 50

    if dia == "miercoles":
        precio = precio / 2

    print("Puedes entrar al cine. Tu precio es: Q", precio)
