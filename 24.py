#Se dispone de una serie de cuaternas de números positivos y se quiere encontrar e imprimir
# la suma mayor de todas las cuaternas. El proceso finalizará cuando el primer elemento de
# alguna cuaterna sea igual a cero 

while(True):
    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))
    numero3 = int(input("Ingresa el numero 3: "))
    numero4 = int(input("Ingresa el numero 4: "))
    suma = numero1 + numero2 + numero3 + numero4
    print(f"La suma da: {suma}")
    if(numero1 == 0):
        break