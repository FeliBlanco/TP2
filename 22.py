#Se dispone de una serie de ternas de números enteros positivos y se quiere calcular e
# imprimir la suma de cada una de ellas, indicando mediante un mensaje si dicha suma es
# Par. Fin de proceso cuando alguna suma sea mayor que setecientos.

while(True):
    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))
    numero3 = int(input("Ingresa el numero 3: "))
    suma = numero1 + numero2 + numero3
    if(suma % 2 == 0):
        print("La suma es par.")
    if(suma > 75):
        break