import requests
import sys


G_usuario = "Teste"
G_senha = "5567"


def brute(usuario, senha):
    if (G_usuario == usuario):
        if (G_senha == senha):
            print("Senha encontrada: ", senha)
            return True
        else:
            #print("Tentantiva falha: ", senha)
            return False   


def main():
	words = [w.strip() for w in open("wordlist.txt", "rb").readlines()] 
	for password in words:
		brute(G_usuario,password)


if __name__ == '__main__':
	main()