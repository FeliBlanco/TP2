#En un comercio se quiere saber cuántos empleados realizaron ventas superiores a cien mil a
# lo largo un mes; para esto se dispone como dato del número de legajo, y el importe
# vendido por cada empleado durante el período controlado

empleados = 0
while(True):
    legajo = int(input("Ingresa el numero de legajo: "))
    if(legajo == 0):
        break
    else:
        importe = float(input("Ingresa el importe: "))
        if(importe > 100000):
            empleados = empleados + 1

print(f"{empleados} empleados realizaron ventas superiores a cienmil.")