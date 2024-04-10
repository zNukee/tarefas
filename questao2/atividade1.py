def verificar_numero(numero):
    if numero < 0:
        print("Retroceder")
    elif numero == 0:
        print("Pare")
    else:
        print("Avançar")

# Solicitar entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verificar e imprimir resultado
verificar_numero(numero)
