#Leer una serie de cincuenta números enteros. Informar cuantos son mayores que 100

i = 0
mayores = 0

while(i < 50):
    numero = int(input("Ingrese un numero:"))
    if(numero > 100):
        mayores = mayores + 1
    i = i + 1

print("Numeros mayores que 100: " + str(mayores))