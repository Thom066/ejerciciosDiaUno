#Pide un número entero. Indica si es par o impar.

numero = 0
numero = int(input("Digita un numero: "))
if (numero % 2) == 0:
    print("El", numero, "es par")
else :
    print("El",numero, "No es par")