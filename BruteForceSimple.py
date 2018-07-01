#import requests
#import sys
import time

start = time.time()
G_usuario = "Teste"
G_senha = "999999"



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
    words = [w.strip() for w in open("wordlist3.txt", "r").readlines()]

    #number_lines = sum(1 for line in open("wordlist4.txt"))
    #print("linhas: ",number_lines)

    #with open("wordlist4.txt") as infile:   //Usar fora para 8 digitos, for dentro do while
    for password in words:

        # password = password.strip()   //Caso use While

        if brute(G_usuario,password) == True:
            break


if __name__ == '__main__':
    main()