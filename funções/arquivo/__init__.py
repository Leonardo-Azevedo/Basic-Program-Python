from funções import principais


def cadastrar():
    escreverArq = open("cadastros.txt", "a")

    while True:
        nome = str(input("Nome: "))
        if principais.alfabetico(nome) == 1:
            break
    idade = principais.tryNumerico("Idade: ")

    escreverArq.write(f"{nome},{idade},Ativo\n")
    escreverArq.close()
    print(f"Novo registro de {nome} adicionado.")
    

def lerTudo():
    arquivoLerTudo = open("cadastros.txt", "r")
    cadastros = arquivoLerTudo.readlines()
    
    txt = "Cadastros"
    print("="*30)
    print(txt.center(30))
    print("="*30)
    for linha in cadastros:
        dado = linha.split(",")
        if 'Ativo' in dado[2]:
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<22}{dado[1]:>3} anos")

    arquivoLerTudo.close()

def deletarCad():
    arquivoLerTudo = open("cadastros.txt", "r")
    cadastros = arquivoLerTudo.readlines()
    
    nomeDelet = str(input("Nome: "))
    for linha in cadastros:
        if nomeDelet in linha:
            posi = cadastros.index(linha)
            cadastros.pop(posi)
            #print(posi)
            reescrever = open("cadastros.txt", "w")
            reescrever.writelines(cadastros)
            reescrever.close()
            return print('Cadastro deletado')
        
    print("Cadastro inexistente.")
    
    arquivoLerTudo.close()