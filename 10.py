#En una oficina meteorológica se dispone de las temperaturas máximas y mínimas diarias, a
# lo largo de un período x. Se quieren encontrar las temperaturas mínima, máxima, la
# máxima de las mínimas y la mínima de las máximas. Se debe ingresar los datos de a pares
# ordenados (mín, max). El proceso termina cuando las temperaturas leídas sean (noventa y
# nueve - noventa y nueve).

temperaturaMax_min = -1

temperaturaMin_max = -1

while(True):
    max = float(input("Ingresa la temperatura maxima: "))
    min = float(input("Ingresa la temperatura minima: "))
    if(max > 99):
        break
    else:
        if(max < temperaturaMax_min):
            temperaturaMax_min = max
        
        if(min > temperaturaMin_max):
            temperaturaMin_max = min
        
print(f"Temperatura máxima de las minimas: {temperaturaMin_max}")
print(f"Temperatura minima de las maximas: {temperaturaMax_min}")
