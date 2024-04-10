def calcular_gotas(concentracao, peso, dose_por_kg):
    dose_total = (peso * dose_por_kg) / concentracao
    quantidade_gotas = dose_total * 20  # 1 ml equivale a aproximadamente 20 gotas
    return quantidade_gotas

# Solicitar entrada do usuário
concentracao = float(input("Digite a concentração do medicamento em mg/ml: "))
peso = float(input("Digite o peso da criança em kg: "))
dose_por_kg = float(input("Digite a dose recomendada em mg por kg: "))

# Calcular quantidade de gotas
gotas_necessarias = calcular_gotas(concentracao, peso, dose_por_kg)

# Exibir resultado
print("A quantidade de gotas necessárias é:", gotas_necessarias)
