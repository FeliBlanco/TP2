#Leer una serie de números cuyo último valor es cero, se pide indicar cuántos valores hay mayores que cien.

mayores100 = 0

while(True):
    numero = int(input("Ingrese un numero: "))
    if(numero == 0):
        break
    else:
        if(numero > 100):
            mayores100 = mayores100 + 1

print(f"Hay {mayores100} numeros mayor que 100.")