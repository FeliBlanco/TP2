#Leer un número y si es múltiplo de cuatro sin serlo de cinco, calcular los diez primeros
# múltiplos de dicho número, sino su mitad, tercera y cuarta parte, imprimiendo los valores
# mientras se calculan.

numero = float(input("Ingrese un numero: "))

if(numero % 4 == 0 and numero % 5 != 0):
    for i in range(10):
        multiplo = i * numero
        print(f"Multiplo #{i}: {multiplo}")
else:
    mitad = numero / 2
    print(f"La mitad: {mitad}")
    tercio = numero / 3
    print(f"Tercio: {tercio}")
    cuarto = numero / 4
    print(f"Cuarta: {cuarto}")
