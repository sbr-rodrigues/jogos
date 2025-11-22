from time import sleep
from random import randint
pedra = "\U0001FAA8"
papel = "\U0001F4C4"
tesoura = "\u2702"
vitoria_emoji = "\U0001F947"
empate_emoji = "\U0001F91D" 
derrota_emoji = "\U0001F494"
itens = [("Pedra", pedra), ("Papel", papel), ("Tesoura", tesoura)]
empates = 0
vitorias = 0
derrotas = 0
while True:
    computador = randint(1, 3)
    print("Suas opções:")
    print(f"[1] {pedra} Pedra")
    print(f"[2] {papel} Papel")
    print(f"[3] {tesoura} Tesoura")

    jogador = int(input("Qual é a sua jogada? "))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!")
    print(f"\nVocê jogou {itens[jogador - 1][1]} {itens[jogador - 1][0]}")
    print(f"Computador jogou {itens[computador - 1][1]} {itens[computador - 1][0]}")
    if computador == 1:
        if jogador == 1:
            print("Computador jogou Pedra")
            print("Empate!")
            empates +=1
            print(f"{empate_emoji} Empates: {empates}")
        elif jogador == 2:
            print("Computador jogou Pedra")
            print("Você ganhou!")
            vitorias +=1
            print(f"{vitoria_emoji} Vitórias: {vitorias}")
        elif jogador == 3:
            print("Computador jogou Pedra")
            print("Computador ganhou!")
            derrotas +=1
            print(f"{derrota_emoji} Derrotas: {derrotas}")
        else:
            print("Jogada inválida!")
    elif computador == 2:
        if jogador == 1:
            print("Computador jogou Papel")
            print("Computador ganhou!")
            derrotas +=1
            print(f"{derrota_emoji} Derrotas: {derrotas}")
        elif jogador == 2:
            print("Computador jogou Papel")
            print("Empate!")
            empates +=1
            print(f"{empate_emoji} Empates: {empates}")
        elif jogador == 3:
            print("Computador jogou Papel")
            print("Você ganhou!")
            vitorias +=1
            print(f"{vitoria_emoji} Vitórias: {vitorias}")
        else:
            print("Jogada inválida!")
    elif computador == 3:
        if jogador == 1:
            print("Computador jogou Tesoura")
            print("Você ganhou!")
            vitorias +=1
            print(f"{vitoria_emoji} Vitórias: {vitorias}")
        elif jogador == 2:
            print("Computador jogou Tesoura")
            print("Computador ganhou!")
            derrotas +=1
            print(f"{derrota_emoji} Derrotas: {derrotas}")
        elif jogador == 3:
            print("Computador jogou Tesoura")
            print("Empate!")
            empates +=1
            print(f"{empate_emoji} Empates: {empates}")
        else:
            print("Jogada inválida!")
    print(f"\nPlacar parcial: {vitorias} Vitórias | {empates} Empates | {derrotas} Derrotas\n")
    while True:
        resp = input("Mais uma partida? [S/N] ").strip().upper()
        if resp == "S":
            break
        elif resp == "N":
            print("Obrigado por jogar! Até a próxima.")
            print("\nObrigado por jogar! Até a próxima.")
            print("\n🏁 Placar final:")
            print(f"{vitoria_emoji} Vitórias: {vitorias}")
            print(f"{empate_emoji} Empates: {empates}")
            print(f"{derrota_emoji} Derrotas: {derrotas}\n")
            exit()
        else:
            print("ERRO! Resposta inválida. Por favor, responda com 'S' ou 'N'.")