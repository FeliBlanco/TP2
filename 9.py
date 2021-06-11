#Para elaborar la misma estadística, se necesita verificar que todos los valores ingresados sean
# mayor ó igual que cero; En caso contrario indicar que se trata de un error; ignorar el dato
# leído y leer el próximo


numeroMayor = -1

while(True):
    numero = int(input("Ingrese un numero: "))
    if(numero >= 0):
        if(numero > 999):
            break
        elif(numero > numeroMayor):
            numeroMayor = numero
    else:
        print("ERROR: Debe ingresar un numero igual o mayor que 0.")