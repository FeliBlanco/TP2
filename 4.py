#. Se dispone de diez pares ordenados (X,y) de números. a los cuales se debe calcular la suma
#de todas las X y la suma de todas las Y, imprimir los resultados

sumaX = 0
sumaY = 0

pares = 0
while(pares < 10):
    pares = pares + 1
    x = int(input("Ingresa un valor para x: "))
    y = int(input("Ingresa un valor para y:"))
    sumaX = sumaX + x
    sumaY = sumaY + y

print(f"Suma de las X: {sumaX}")
print(f"Suma de las Y: {sumaY}")