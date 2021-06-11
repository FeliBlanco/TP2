#Leer de a uno, una serie de números enteros, e imprimir un “*” al lado de cada número par.
# El proceso termina cuando el número leído sea cero.

while(True):
    numero = int(input("Ingrese un numero: "))
    if(numero == 0):
        break
    else:
        if(numero % 2 == 0):
            print(f"*{numero}")
        else:
            print(str(numero))