#import requests
#import sys
import time

G_usuario = "Teste"
G_senha = "99999999"
start = time.time()


def brute(usuario, senha):
    if (G_usuario == usuario):
        if (G_senha == senha):
            print("Senha encontrada: ", senha)
            tempo_execucao = time.time() - start

            #a = time.strftime("%H:%M:%S", time.gmtime(tempo_execucao))
            print("Tempo de Execução: ", tempo_execucao)
            return True
        else:
            #print("Tentantiva falha:", senha)
            return False   

def main():
    #words = [w.strip() for w in open("wordlist4.txt", "r").readlines()]


    with open("wordlist4.txt") as infile:
        for password in infile:
            password = password.strip()
            #brute(G_usuario,password)
            if brute(G_usuario,password) == True:
                break


if __name__ == '__main__':
    main()