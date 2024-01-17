import random

def jogar():
    print("****************************************")
    print("Bem vindo ao meu primeiro jogo em Python")
    print("       Um jogo de adivinhação!")
    print("****************************************")

    numero_secreto = round(random.randrange(1,101))
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Em que nível de dificuldade jogará?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o Nível: "))

    while(nivel<1 or nivel>3):
        nivel = int(input("Defina o Nível: "))
        print("Digite um número entre 1 e 3")
        continue
    print(f"Você selecionou o nivel {nivel}")
    if(nivel == 1):
        max_tentativas = 12
    elif(nivel == 2):
        max_tentativas = 8
    else:
        max_tentativas = 5

    for rodada in range(1,max_tentativas+1):
        print("Essa é a rodada {} de {}".format(rodada,max_tentativas))
        if(rodada == max_tentativas):
            print("Essa é sua última rodada!")
        chute_str = input("Digite um número entre 1 e 100 para começar o jogo! ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        print("Você digitou", chute)

        acertou = numero_secreto == chute
        maior   = numero_secreto < chute
        menor   = numero_secreto > chute

        if(acertou):
            print("Você acertou na sua {} rodada e fez {} pontos, Parabéns!".format(rodada, pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior que o número secreto")
                if (rodada == max_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou, o seu chute foi menor que o número secreto")
                if (rodada == max_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = round(abs(numero_secreto - chute)/ 3)
            pontos = pontos - pontos_perdidos
            print(f"Você perdeu {pontos_perdidos}")
        tentativas = tentativas + 1
        rodada = rodada + 1

    print("Fim de jogo")
if (__name__ == "__main__"):
    jogar()