#Ídem al problema anterior, pero esta vez, el fin del proceso está dado cuando el importe 
# mayor supere los mil.

vendedorMax = [0, 0]
vendedorMin = [0, 0]

while(True):
    vendedor = int(input("Ingrese el codigo del vendedor: "))
    importe = int(input("Ingrese el valor del importe: "))
    if(importe > 100):
        break
    else:
        if(importe >= vendedorMax[0]):
            vendedorMax[0] = importe
            vendedorMax[1] = vendedor

        if(importe <= vendedorMin[0]):
            vendedorMin[0] = importe
            vendedorMin[1] = vendedor

print(f"El vendedor de mayor importe fue: #{vendedorMax[1]}")
print(f"El vendedor de menor importe fue: #{vendedorMin[1]}")
