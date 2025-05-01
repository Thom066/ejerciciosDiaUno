#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

totalCuenta = float(input("Cual es el total de la cuenta?: " ))
print("Que porcentaje de propina desea dejar?: puedes elegir entre 10, 15 o 20")

porcentajePropina = int(input("Introduce el porcentaje de propina: "))

if porcentajePropina == 10 or porcentajePropina == 15 or porcentajePropina ==20:
    propina = totalCuenta * (porcentajePropina / 100)
    print(f"la propina que debes dejar es: $ {propina:.2f}")
else :
    print("La opcion no es valida tienes que escoger entre 10, 15 o 20")