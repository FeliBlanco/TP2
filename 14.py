#En un instituto de enseñanza, se quiere emitir un listado de todos aquellos alumnos que el
# promedio general sea superior a siete, para lo cual se ingresa como dato: número de legajo
# y los promedios de las cuatro materias que se dictan. Terminar el proceso cuando se lea
# un número de legajo igual a cero.

while(True):
    legajo = int(input("Ingresa el numero de legajo: "))
    if(legajo == 0):
        break
    else:
        materia1 = float(input("Ingrese el promedio de la materia 1: "))
        materia2 = float(input("Ingrese el promedio de la materia 2: "))
        materia3 = float(input("Ingrese el promedio de la materia 3: "))
        materia4 = float(input("Ingrese el promedio de la materia 4: "))
        promedio = (materia1 + materia2 + materia3 + materia4) / 4
        if(promedio > 7):
            print(f"Alumno legajo: {legajo}.")