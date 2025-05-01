#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

print("Digita dos numeros")

numero1 = input()
numero1 = int(numero1)

numero2 = input()
numero2 = int(numero2)

if numero1 > numero2:
    print("El numero",numero1,"es mayor")
elif numero1 == numero2:
    print("Los numeros son iguales")
else :
    print("El numero",numero2,"es mayor")