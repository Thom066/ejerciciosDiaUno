#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

año = int(input("Digita un año: "))

if año % 4 == 0 and not (año % 100 == 0):
    print("El año es Bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("El año es Bisiesto")
elif not año % 4 == 0:
    print("El año es normal")
else :
    print ("El año es normal")