#Para poder extraer alguna estadística, en una agencia de quiniela, se requiere saber cuál fue
# el mayor valor registrado en los sorteos comprendidos en un periodo de tiempo
# determinado, Terminar el proceso de carga de los números, cuando el valor leído sea
# mayor que novecientos noventa y nueve.

numeroMayor = -1

while(True):
    numero = int(input("Ingresa un numero: "))
    if(numero > 999):
        break
    elif(numero > numeroMayor):
        numeroMayor = numero

#no pidió imprimir el valor del numero mayor, pero en otro caso, descomentar
#print(f"Numero mayor: {numeroMayor}")