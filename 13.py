#Leer un número calcular la raíz cúbica y así sucesivamente hasta que el resultado sea menor
# o igual qué uno, imprimir los resultados parciales y finales. Controlar que el número Ieido
# sea mayor que cero al comenzar el proceso.

import numpy as np

while(True):
    numero = int(input("Ingrese un numero: "))
    if(numero > 0):
        raizCubica = np.cbrt(numero)
        print(f"La raiz cubica de {numero} es: {raizCubica}")
        if(raizCubica <= 1):
            break