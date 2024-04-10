def mover_elevador(andar_atual, andar_destino):
    if andar_destino > andar_atual:
        print("Subindo")
    elif andar_destino < andar_atual:
        print("Descendo")
    else:
        print("Parado")

# Inicializar o elevador no andar 0
andar_atual = 0

# Loop infinito para solicitar os próximos andares
while True:
    # Solicitar entrada do usuário
    andar_destino = int(input("Digite o próximo andar desejado (ou '0' para sair): "))
    
    # Verificar e imprimir a direção do elevador
    if andar_destino == 0:
        print("Programa encerrado.")
        break
    mover_elevador(andar_atual, andar_destino)
    andar_atual = andar_destino
