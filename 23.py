#. Se dispone de una serie de temas de números enteros positivos y se quiere calcular e
# imprimir la suma de cada una de ellas, indicando mediante un mensaje si dicha suma es
# múltiplo de nueve. Finalizar el proceso cuando una suma sea igual a cero.

while(True):
    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))
    numero3 = int(input("Ingresa el numero 3: "))
    suma = numero1 + numero2 + numero3
    if(suma % 9 == 0):
        print("La suma es multiplo de 9.")
    if(suma == 0):
        break