from time import sleep
from random import randint

itens = ("\033[1;30;42mPEDRA\033[m", "\033[1;30;42mPAPEL\033[m", "\033[1;30;42mTESOURA\033[m")

while True:
    print('''\033[1;30;42mSuas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA\033[m''')

    try:
        jog = int(input("\033[1;32mQual é a sua jogada? \033[m"))
        if jog not in [0, 1, 2]:
            raise ValueError 
    except ValueError:
        print("\033[1;30;41mJOGADA INVÁLIDA!!!\033[m")
        continue 

    comp = randint(0, 2)

    for palavra in ["\033[1;32mJO\033[m", "\033[1;32mKEN\033[m", "\033[1;32mPÔ!!!\033[m"]:
        print(palavra)
        sleep(1)

    print("=-" * 11)
    print(f"Computador jogou {itens[comp]}")
    print(f"Jogador jogou {itens[jog]}")
    print("=-" * 11)

    if comp == jog:
        print("\033[1;30;43mEMPATE!!!\033[m")
    elif (comp == 0 and jog == 1) or (comp == 1 and jog == 2) or (comp == 2 and jog == 0):
        print("\033[1;30;42m Você VENCEU!!!\033[m")
    else:
        print("\033[1;30;41mVocê PERDEU!!!\033[m")

    while True:
        jogar_novamente = input("Quer jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente in ["S", "N"]:
            break
        else:
            print("\033[1;30;43mOpção inválida! Por favor, digite S para jogar novamente ou N para sair.\033[m")

    if jogar_novamente == "N":
        print("\033[1;30;42mObrigado por jogar! Até a próxima. 😃\033[m")
        break

