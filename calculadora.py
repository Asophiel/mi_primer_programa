
operacion = input("Que operacion deseas realizar? (Multiplicar/Dividir/Restar/Sumar)").upper()
numero_del_usuario_1 = int(input("Dime el primer numero"))
numero_del_usuario_2 = int(input("Dime el segundo numero"))

if operacion == "MULTIPLICAR":
    print(int(numero_del_usuario_1) * int(numero_del_usuario_2))
elif operacion == "DIVIDIR":
    print(int(numero_del_usuario_1) / int(numero_del_usuario_2))
elif operacion == "RESTAR":
    print(int(numero_del_usuario_1) - int(numero_del_usuario_2))
elif operacion == "SUMAR":
    print(int(numero_del_usuario_1) + int(numero_del_usuario_2))











