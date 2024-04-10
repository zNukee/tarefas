def verificar_cor(cor):
    if cor.lower() == "vermelho":
        print("Pare")
    elif cor.lower() == "amarelo":
        print("Atenção")
    elif cor.lower() == "verde":
        print("Siga")
    else:
        print("Cor desconhecida")

# Solicitar entrada do usuário
cor = input("Digite uma cor (verde, amarelo ou vermelho): ")

# Verificar e imprimir mensagem correspondente à cor
verificar_cor(cor)
