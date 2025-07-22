dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año: "))

if mes < 1 or mes > 12:
    print("Fecha inválida: el mes debe estar entre 1 y 12.")
else:
    esBisiesto = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        esBisiesto = True

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        diaMes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        diaMes = 30
    elif mes == 2:
        if esBisiesto:
            diaMes = 29
        else:
            diaMes = 28

    # Verificar si el día es válido
    if dia < 1 or dia > diaMes:
        print("El día no es válido para ese mes.")
    else:
        month = mes
        year = ano
        if month == 1 or month == 2:
            month = month + 12
            year = year - 1

        q = dia
        k = year % 100
        j = year // 100

        h = (q + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

        if h == 0:
            diaSemana = "sábado"
        elif h == 1:
            diaSemana = "domingo"
        elif h == 2:
            diaSemana = "lunes"
        elif h == 3:
            diaSemana = "martes"
        elif h == 4:
            diaSemana = "miércoles"
        elif h == 5:
            diaSemana = "jueves"
        elif h == 6:
            diaSemana = "viernes"
        print("La fecha", dia, "/", mes, "/", ano, "fue un", diaSemana)
