def calcular_valor_parcela(valor_total, num_parcelas):
    valor_parcela = valor_total / num_parcelas
    return valor_parcela

# Solicitar entrada do usuário
valor_total = float(input("Digite o valor total da compra: "))
num_parcelas = int(input("Digite o número de parcelas: "))

# Calcular o valor de cada parcela
valor_parcela = calcular_valor_parcela(valor_total, num_parcelas)

# Exibir resultado
print("O valor de cada parcela é: R$", valor_parcela)
