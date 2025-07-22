print("Comparador de fechas (tipo calendario digital)")
print("Primera fecha:")
dia1 = int(input("Día: "))
mes1 = int(input("Mes: "))
ano1 = int(input("Año: "))

print("\nSegunda fecha:")
dia2 = int(input("Día: "))
mes2 = int(input("Mes: "))
ano2 = int(input("Año: "))

if ano1 > ano2:
    mayor = "La primera fecha es mayor."
elif ano1 < ano2:
    mayor = "La segunda fecha es mayor."
else:
    if mes1 > mes2:
        mayor = "La primera fecha es mayor."
    elif mes1 < mes2:
        mayor = "La segunda fecha es mayor."
    else:
        if dia1 > dia2:
            mayor = "La primera fecha es mayor."
        elif dia1 < dia2:
            mayor = "La segunda fecha es mayor."
        else:
            mayor = "Ambas fechas son iguales."

if ano1 == ano2 and mes1 == mes2:
    mismoMesAnio = "Las fechas están en el mismo mes y año."
else:
    mismoMesAnio = "Las fechas NO están en el mismo mes y año."

dias1 = ano1 * 365 + mes1 * 30 + dia1
dias2 = ano2 * 365 + mes2 * 30 + dia2
diferencia = dias1 - dias2


print("\n--- Resultados ---")
print(mayor)
print(mismoMesAnio)
print("Diferencia de días (aproximada):", diferencia)
