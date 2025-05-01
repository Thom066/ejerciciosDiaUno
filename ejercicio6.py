#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

numeroSecreto = 7

print("Digita tu nombre")

nombreUsuario = input()

print("Bienvenido",nombreUsuario,"Intenta adivinar el numero secreto que esta entre el 1 y el 100")

print("Digita un numero: ")

adivinacion = input()
adivinacion = int(adivinacion)

if adivinacion > numeroSecreto:
    print("El que has puesto es mayor")
elif adivinacion < numeroSecreto:
    print("El numero que has puesto es menor")
else :
    print("Adivinaste el numero") 