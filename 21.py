#Ingresar por teclado de a uno una serie de números. Encontrar e imprimir el menor de los
# números pares. La cantidad de elementos leídos es cien.
numeroMenor = 0

i = 0
while(i < 100):
    i = i + 1
    numero = int(input("Ingrese un numero: "))
    if(numero == 0):
        break
    else:
        if(numero % 2 == 0):
            if(numero < numeroMenor):
                numeroMenor = numero
print(f"El numero menor de los pares es {numeroMenor}")