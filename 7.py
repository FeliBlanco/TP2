#En una serie de treinta y cuatro elementos, se quiere calcular e imprimir el cuadrado de cada número, deberán ser leído dos uno por vez


i = 0

while(i < 34):
    i = i + 1
    numero = int(input("Ingresa un numero: "))
    cuadrado = numero * numero
    print(f"Su cuadrado es: {cuadrado}")