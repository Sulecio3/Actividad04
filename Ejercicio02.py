print("Calculadora de impuestos progresivos + deducciones")
ingreso = float(input("Ingreso anual: "))
dependientes = int(input("Número de dependientes: "))

deduccion = dependientes * 1000
ingresoFijo= ingreso - deduccion
if ingresoFijo < 0:
    ingresoFijo = 0

if ingreso < 40000 and dependientes > 2:
    print("No paga impuestos")
else:
    if ingresoFijo <= 30000:
        impuesto = ingresoFijo * 0.05
    elif ingresoFijo <= 60000:
        impuesto = 1500 + (ingresoFijo - 30000) * 0.10
    elif ingresoFijo <= 100000:
        impuesto = 4500 + (ingresoFijo - 60000) * 0.15
    else:
        impuesto = 10500 + (ingresoFijo - 100000) * 0.20

    print(f"Impuesto a pagar: Q{impuesto}")