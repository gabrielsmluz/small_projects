
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False


    while(not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper == letra.upper):
                letras_acertadas[index] = letra
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print(letras_acertadas)
        print("Jogando...")
        

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()