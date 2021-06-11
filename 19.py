#. Ingresar de a uno una serie de números. Encontrar e Imprimir el mayor de todos los números
# pares, el proceso terminará cuando el número leído sea igual a cero

numeroMayor = 0

while(True):
    numero = int(input("Ingrese un numero: "))
    if(numero == 0):
        break
    else:
        if(numero % 2 == 0):
            if(numero > numeroMayor):
                numeroMayor = numero
print(f"El numero mayor de los pares es {numeroMayor}")