#En una empresa se desea saber cuántos empleados tienen un sueldo superior a mil. Se
# dispone como dato el número del legajo y el sueldo de cada uno de los empleados. El
# proceso termina cuando el número de legajo lerdo sea igual a cero

empleados = 0

while(True):
    legajo = int(input("Ingresa el numero de legajo: "))
    if(legajo == 0):
        break
    else:
        sueldo = int(input("Ingresa el sueldo: "))
        if(sueldo > 1000):
            empleados = empleados + 1
print(f"{empleados} tienen el sueldo mayor a 1000.")