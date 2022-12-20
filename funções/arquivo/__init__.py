from funções import principais



def cadastrar():

    escreverArq = open("cadastros.txt", "a")

    while True:
        nome = str(input("Nome: "))
        if principais.alfabetico(nome) == 1:
            break
    idade = principais.tryNumerico("Idade: ")

    escreverArq.write(f"{nome},{idade}\n")
    print(f"Novo registro de {nome} adicionado.")
    escreverArq.close()

def lerTudo():
    arquivoLerTudo = open("cadastros.txt", "r")

    cadastros = arquivoLerTudo.readlines()

    txt = "Cadastros"
    print("="*30)
    print(txt.center(30))
    print("="*30)
    for linha in cadastros:
        dado = linha.split(",")
        dado[1] = dado[1].replace("\n", "")
        print(f"{dado[0]:<22}{dado[1]:>3} anos")

    arquivoLerTudo.close()