def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(101):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar entrada do usuário
numero = int(input("Digite um número para gerar a tabuada: "))

# Gerar e imprimir a tabuada
tabuada(numero)
