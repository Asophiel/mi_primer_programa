# Recuerda que tienes que elegir un numero para que lo adivine tu amigo sino el juego no tiene sentido

numero = input("Elige un numero para que tu amigo lo adivine")
adivinanza = input("Itentas adivinar el numero de tu amigo")

while numero != adivinanza:
    print("Erraste intenta denuevo")
    adivinanza = input("Itentas adivinar el numero de tu amigo")

print("Adivinaste, has ganado, felicitaciones")
