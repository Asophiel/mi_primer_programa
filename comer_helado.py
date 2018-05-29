queres_un_helado_input = input("Queres un helado? (Si/No)").upper()

if queres_un_helado_input == "SI":
    queres_un_helado = True
elif queres_un_helado_input == "NO":
    queres_un_helado = False
else:
    print("Te dije que pongas si o no, ahora cuento tu respuesta como un no")
    queres_un_helado = False
tenes_plata_input = input ("Tenes plata para un helado? (Si/No)").upper()
esta_la_heladeria_input = input("Esta la heladeria abierta? (Si/No)").upper()
esta_tu_tia_input = input ("Esta tu tia en casa? (Si/No)").upper()


queres_un_helado  = queres_un_helado_input == "SI"
tenes_plata =  tenes_plata_input == "SI"
esta_tu_tia_ = esta_tu_tia_input == "SI"
podes_comprarlo = tenes_plata_input or esta_tu_tia_input
esta_la_heladeria = esta_tu_tia_input == "SI"

if queres_un_helado and podes_comprarlo and esta_la_heladeria:
    print("Comprate un healdo")
else:
    print("Boosteaste")



