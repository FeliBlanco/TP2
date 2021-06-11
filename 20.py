#Ingresar de a uno, una serie de números. Encontrar e imprimir el mayor de todos los números
# pares cuyo número de orden sea par, el proceso terminará cuando el número lerdo sea igual a cero

numeroMayor = 0
numeroOrden = 0

while(True):
    numero = int(input("Ingrese un numero: "))
    numeroOrden = numeroOrden + 1
    if(numero == 0):
        break
    else:
        if(numero % 2 == 0):
            if(numero > numeroMayor and numeroOrden % 2 == 0):
                numeroMayor = numero
print(f"El numero mayor de los pares es {numeroMayor}")