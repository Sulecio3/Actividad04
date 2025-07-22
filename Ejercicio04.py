print("Simulador de facturación con IVA, descuentos y propina")
precio1 = float(input("Precio del producto 1: "))
precio2 = float(input("Precio del producto 2: "))
precio3 = float(input("Precio del producto 3: "))
subtotal = precio1 + precio2 + precio3

preguntaPropina = input("¿Desea dejar propina? (s/n): ").lower()
if preguntaPropina == "s":
    porcentaje = float(input("Porcentaje de propina: "))
    propina = subtotal * (porcentaje / 100)
else:
    propina = 0

preguntaTarjeta = input("¿Tiene tarjeta de descuento? (s/n): ").lower()
if preguntaTarjeta == "s":
    descuento = subtotal * 0.10
else:
    descuento = 0

iva = (subtotal - descuento) * 0.12
total = subtotal - descuento + iva + propina

print("\n--- FACTURA ---")
print("Producto 1:", precio1)
print("Producto 2:", precio2)
print("Producto 3:", precio3)
print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("IVA (12%):", iva)
print("Propina:", propina)
print("TOTAL:", total)