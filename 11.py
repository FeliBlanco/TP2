#En un comercio hay cuatro vendedores y quieren saber, cuál fue el que realizó la venta de
# mayor importe, y cual la venta de menor importe. Terminar el proceso cuando el importe
# leído sea cero. los datos se leerán de a pares (Codven, Imp).

vendedorMax = [0, 0]
vendedorMin = [0, 0]

while(True):
    vendedor = int(input("Ingrese el codigo del vendedor: "))
    importe = int(input("Ingrese el valor del importe: "))
    if(importe == 0):
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
