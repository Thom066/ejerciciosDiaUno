#Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = int(input("Digita un numero: "))
if numero > 0:
    print("El numero:",numero, "Es POSITIVO")
elif numero <0:
    print("El numero:",numero, "Es NEGATIVO")
else :
    print("El numero:",numero, "Es 0")