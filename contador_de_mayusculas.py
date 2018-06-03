
frase_usurio = input("Introduce una frase:")
mayusculas = (frase_usurio).upper()
numero_mayusculas = 0

for letra in frase_usurio:
    if letra in mayusculas:
        numero_mayusculas += 1
print("Mayusculas: {}".format(numero_mayusculas))




