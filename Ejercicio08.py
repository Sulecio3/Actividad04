print("Calculadora de rumbo entre puntos cardinales")
inicio = input("Desde dónde parte (norte/sur/este/oeste): ").lower()
destino = input("Hacia dónde va (norte/sur/este/oeste): ").lower()

if inicio == destino:
    print("Ya estás en esa dirección. No necesitas moverte.")
elif inicio == "norte" and destino == "sur":
    print("Debes ir recto hacia el sur.")
elif inicio == "sur" and destino == "norte":
    print("Debes ir recto hacia el norte.")
elif inicio == "este" and destino == "oeste":
    print("Debes ir recto hacia el oeste.")
elif inicio == "oeste" and destino == "este":
    print("Debes ir recto hacia el este.")
elif (inicio == "norte" and destino == "este") or (inicio == "este" and destino == "norte"):
    print("Debes ir hacia el noreste.")
elif (inicio == "norte" and destino == "oeste") or (inicio == "oeste" and destino == "norte"):
    print("Debes ir hacia el noroeste.")
elif (inicio == "sur" and destino == "este") or (inicio == "este" and destino == "sur"):
    print("Debes ir hacia el sureste.")
elif (inicio == "sur" and destino == "oeste") or (inicio == "oeste" and destino == "sur"):
    print("Debes ir hacia el suroeste.")
else:
    print("Dirección no válida. Asegúrate de escribir norte, sur, este u oeste.")
