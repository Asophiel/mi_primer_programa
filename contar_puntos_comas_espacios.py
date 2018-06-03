
frase_usuario = input("Escribe una frase:")
coma = ","
punto = "."
espacio = " "

numero_coma = 0
numero_espacio = 0
numero_punto = 0


for letra in frase_usuario:
    if letra == coma:
        numero_coma += 1
    elif letra == punto:
        numero_punto += 1
    elif letra == espacio:
        numero_espacio += 1

print("Espacios: {}".format(numero_espacio))
print("Comas: {}".format(numero_coma))
print("Puntos: {}".format(numero_punto))

