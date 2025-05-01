#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:
# "Bajo peso" si es menor a 18.5
# "Normal" si está entre 18.5 y 24.9
# "Sobrepeso" si está entre 25 y 29.9
# "Obesidad" si es mayor o igual a 30


#print("Digita tu peso:")
#pesoKg = input()
#pesoKg = int(pesoKg)

#print("Muy bien, ahora digita tu altura: ")
#alturaM = input()
#alturaM = float(pesoKg)

pesoKg = int(input("ingresa tu peso (kg): "))
alturaM = float(input("ingresa tu altura (m): "))

resultadoIMC = pesoKg / alturaM**2
print("Tu IMC es:",resultadoIMC)

if resultadoIMC < 18.5:
    print("Bajo peso")
#elif resultadoIMC == 18.5 in 24.9:
elif 18.5 <= resultadoIMC <= 24.9:
    print("Tu peso es normal")
#elif resultadoIMC == 25 in 29.9:
elif 25 <= resultadoIMC <= 29.9:
    print("Estas en sobrepeso")
else :
    print("Estas en Obesidad")


