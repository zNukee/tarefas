def converter_copos_para_ml(quantidade_copos):
    quantidade_ml = quantidade_copos * 200
    return quantidade_ml

# Solicitar entrada do usuário
quantidade_copos = float(input("Digite a quantidade de copos: "))

# Converter copos para mililitros
quantidade_ml = converter_copos_para_ml(quantidade_copos)

# Exibir resultado
print("A quantidade correspondente em mililitros é:", quantidade_ml, "ml")
