
versus = input("Contra que pokemon quieres luchar? (Bulbasaur/Squirtle/Charmander)").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if versus == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "SQUIRTLE"
    ataque_pokemon = 8
elif versus == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "CHARMANDER"
    ataque_pokemon = 7
elif versus == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "BULBASAUR"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Elige un ataque (Chispazo/Bola Voltio)").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
    print("La vida del {} ahores es {}".format(nombre_pokemon, vida_enemigo))
    print("{} te hace {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida de Pikachu ahora es {}".format(vida_pikachu))

if vida_pikachu  <= 0:
    print("¡Has perdido!")
if vida_enemigo <= 0:
    print("¡Has ganado, felicitaciones!")

print("¡El combate ha finalizado!")