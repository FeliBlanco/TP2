#Ingresando un número como dato, imprimir de sus primeros cincuenta múltiplos, que no
# sean a la vez múltiples de seis.

numero = int(input("Ingrese un numero: "))

i = 0
multiplo = 0
while(i < 50):
    if(numero % multiplo == 0 and numero % 6 != 0):
        i = i + 1
    multiplo = multiplo + 1
