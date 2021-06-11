#Leer una serie de números enteros. que contenga como máximo veinte elementos, en caso de
# ingresar un valor negativo o la cantidad de números ingresados supere los veinte, detener
# el proceso e informar mediante un mensaje cuántos son mayores que 100.

i = 0
mayores100 = 0
while(i < 20):
    i = i + 1
    numero = int(input("Ingresa un numero: "))
    if(numero >= 0):
        if(numero > 100):
            mayores100 = mayores100 + 1
    else:
        break

print(f"Hay {mayores100} numeros mayores que 100.")