#se debe calcular e imprimir el producto de todas las X Y de todas las y de cincuenta pares
#ordenados de números enteros.

productoX = 0
productoY = 0

anteriorX = 1
anteriorY = 1

pares = 0
while(pares < 50):
    pares = pares + 1
    x = int(input("Ingresa un valor para x: "))
    y = int(input("Ingresa un valor para y:"))
    productoX = productoX + (x * anteriorX)
    productoY = productoY + (y * anteriorY)
    anteriorX = x
    anteriorY = y

print(f"Suma de las X: {productoX}")
print(f"Suma de las Y: {productoY}")