def calcular_total_compras():
    total = 0
    while True:
        preco = input("Digite o preço do produto ou 'igual' para finalizar: ")
        if preco.lower() == 'igual':
            break
        try:
            preco = float(preco)
            total += preco
        except ValueError:
            print("Por favor, insira um preço válido.")
    return total

# Calcular o total das compras
total_compras = calcular_total_compras()

# Exibir o valor total das compras
print("O valor total das compras é: R$", total_compras)
