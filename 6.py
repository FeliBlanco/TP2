#Leer cien pares ordenados (X,V) de números, y de cada par, imprimir el cociente (cociente = X/Y).

i = 0
while(i < 100):
    i = i + 1
    x = int(input("Ingrese un valor para x:"))
    y = int(input("Ingrese un valor para y:"))
    cociente = x / y
    print(f"cociente: {cociente}")