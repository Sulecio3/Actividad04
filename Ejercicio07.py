print("Sistema de calificaciones con curva")
print("Estudiante 1")
nombre1 = input("Nombre: ")
n11 = float(input("Nota 1: "))
n12 = float(input("Nota 2: "))
n13 = float(input("Nota 3: "))
prom1 = (n11 + n12 + n13) / 3

print("\nEstudiante 2")
nombre2 = input("Nombre: ")
n21 = float(input("Nota 1: "))
n22 = float(input("Nota 2: "))
n23 = float(input("Nota 3: "))
prom2 = (n21 + n22 + n23) / 3

print("\nEstudiante 3")
nombre3 = input("Nombre: ")
n31 = float(input("Nota 1: "))
n32 = float(input("Nota 2: "))
n33 = float(input("Nota 3: "))
prom3 = (n31 + n32 + n33) / 3

print("\nEstudiante 4")
nombre4 = input("Nombre: ")
n41 = float(input("Nota 1: "))
n42 = float(input("Nota 2: "))
n43 = float(input("Nota 3: "))
prom4 = (n41 + n42 + n43) / 3

print("\nEstudiante 5")
nombre5 = input("Nombre: ")
n51 = float(input("Nota 1: "))
n52 = float(input("Nota 2: "))
n53 = float(input("Nota 3: "))
prom5 = (n51 + n52 + n53) / 3

if prom1 < 70 and prom2 < 70 and prom3 < 70 and prom4 < 70 and prom5 < 70:
    print("\nAplicando curva de +5 puntos (máximo 100)...")

    if n11 + 5 > 100:
        n11 = 100
    else:
        n11 = n11 + 5

    if n12 + 5 > 100:
        n12 = 100
    else:
        n12 = n12 + 5

    if n13 + 5 > 100:
        n13 = 100
    else:
        n13 = n13 + 5

    prom1 = (n11 + n12 + n13) / 3

    if n21 + 5 > 100:
        n21 = 100
    else:
        n21 = n21 + 5

    if n22 + 5 > 100:
        n22 = 100
    else:
        n22 = n22 + 5

    if n23 + 5 > 100:
        n23 = 100
    else:
        n23 = n23 + 5

    prom2 = (n21 + n22 + n23) / 3

    if n31 + 5 > 100:
        n31 = 100
    else:
        n31 = n31 + 5

    if n32 + 5 > 100:
        n32 = 100
    else:
        n32 = n32 + 5

    if n33 + 5 > 100:
        n33 = 100
    else:
        n33 = n33 + 5

    prom3 = (n31 + n32 + n33) / 3

    if n41 + 5 > 100:
        n41 = 100
    else:
        n41 = n41 + 5

    if n42 + 5 > 100:
        n42 = 100
    else:
        n42 = n42 + 5

    if n43 + 5 > 100:
        n43 = 100
    else:
        n43 = n43 + 5

    prom4 = (n41 + n42 + n43) / 3

    if n51 + 5 > 100:
        n51 = 100
    else:
        n51 = n51 + 5

    if n52 + 5 > 100:
        n52 = 100
    else:
        n52 = n52 + 5

    if n53 + 5 > 100:
        n53 = 100
    else:
        n53 = n53 + 5

    prom5 = (n51 + n52 + n53) / 3

print("\n--- Tabla Final ---")
print(nombre1, "Promedio:", prom1, 2)
print(nombre2, "Promedio:", prom2, 2)
print(nombre3, "Promedio:", prom3, 2)
print(nombre4, "Promedio:", prom4, 2)
print(nombre5, "Promedio:", prom5, 2)