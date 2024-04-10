def imprimir_mensagem_motivacional(hora):
    if 8 <= hora < 10:
        print("Bom dia! Você consegue alcançar seus objetivos!")
    elif 10 <= hora < 14:
        print("Hora do almoço! Recarregue suas energias para continuar avançando!")
    elif 14 <= hora < 17:
        print("Boa tarde! Persista nos seus esforços, você está no caminho certo!")
    else:
        print("Ainda não tem uma mensagem motivacional definida para este horário.")

# Solicitar entrada do usuário
hora_atual = int(input("Digite a hora atual (em formato 24 horas): "))

# Imprimir mensagem motivacional
imprimir_mensagem_motivacional(hora_atual)
