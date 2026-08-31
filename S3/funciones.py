import os

#Estacion 1
# def convertir_a_dolares(cordobas):
#     tasa = 36.80
#     return cordobas / tasa

# os.system("cls")
# monto = float(input("Monto en córdobas: "))
# resultado = convertir_a_dolares(monto)
# print("Equivalente en dólares:", round(resultado, 2))

#Estacion 2
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal, porcentaje):
    return subtotal*(1-porcentaje)

precio = float(input("Precio unitario C$: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento: "))
subtotal = aplicar_descuento(calcular_subtotal(precio, cantidad), descuento)
print("Subtotal C$:", subtotal)

