print("Clasificador de envío con múltiples condiciones")
peso = float(input("Ingrese el peso del paquete en kg: "))
distancia = float(input("Ingrese la distancia en km: "))
urgente = input("¿El envío es urgente? (sí/no): ").lower()
tamano = input("Tamaño del paquete (pequeño/mediano/grande): ").lower()

costo = peso + distancia

recargoUrgente = 0
recargoTamano = 0
descuento = 0

if urgente == "sí":
    recargoUrgente = 50

if tamano == "grande":
    recargoTamano = 30

if urgente == "no" and peso < 5:
    descuento = 20

total = costo + recargoUrgente + recargoTamano - descuento
print("\n--- Desglose del costo ---")
print("Costo base: Q", costo)
print("Recargo por urgencia: Q", recargoUrgente)
print("Recargo por tamaño: Q", recargoTamano)
print("Descuento: Q", descuento)
print("Total a pagar: Q", total)