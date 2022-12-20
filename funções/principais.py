from funções.arquivo import *
from time import sleep

def alfabetico(nome):
    restrito = nome.replace(" ", "")
    if restrito.isalpha():
        return 1
    else:
        print("Invalido")
        return 0

def tryNumerico(msg):
    while True:
        try:
            leitura = int(input(msg))
        except (ValueError, TypeError):
            print("Digite um valor valido")
        except (KeyboardInterrupt):
            print("Usuario nao digitou")
        else:
            return leitura

def Menu():
    while True:
        txt = "Menu Principal"
        print("="*30)
        print(txt.center(30))
        print("="*30)
        print("[1]Cadastrar")
        print("[2]Listar")
        print("[3]Sair")
        print("="*30)
        op = tryNumerico("Opção: ")
        return op


def verify():
    while True:
        opc = Menu()
        if  opc == 1:
            cadastrar()
        if opc == 2:
            lerTudo()
            print()
            print("Pressione enter...")
            input()
        if opc == 3:
            sleep(0.6)
            print("Saindo...")
            break
        if opc > 3:
            print("Opção nao existe.")