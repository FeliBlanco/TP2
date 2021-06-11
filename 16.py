#Leer por teclado una serie de valores, imprimiendo para cada valor su raíz cuadrada si es par
# y su cuadrado si es impar. Ultimo valor, cero (no debe ser procesado).
import numpy as np

while(True):
    numero = int(input("Ingresa un valor: "))
    if(numero == 0):
        break
    else:
        if(numero % 2 == 0):
            raizCubica = np.cbrt(numero)
            print(f"Raiz cubica de {numero}: {raizCubica}")
        else:
            cuadrado = numero * numero
            print(f"El cuadrado de {numero}: {cuadrado}")