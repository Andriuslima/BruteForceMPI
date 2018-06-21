import requests
import sys
from mpi4py import MPI
import numpy

G_usuario = "Teste"
G_senha = "5567"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def brute(usuario, senha):
    if G_usuario == usuario:
        if G_senha == senha:
            print("Senha encontrada: ", senha)
            return True
        else:
            #print("Tentantiva falha: ", senha)
            return False

def numberOfLines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

def main():
    words = [w.strip() for w in open("wordlist.txt", "rb").readlines()]


    if rank == 0:
        data = "Senha encontrada no core 0"
        for password in words(range(0,numberOfLines(words)/2)):
            if comm.Recv:
                break

            if brute(G_usuario, password):
                comm.send(data, dest=1, tag=11)


    elif rank == 1:
        data = "Senha encontrada no core 1"
        for password in words(range(numberOfLines(words) / 2), numberOfLines(words)):
            if comm.Recv:
                break

            if brute(G_usuario, password):
                comm.send(data, dest=0,tag=11)


if __name__ == '__main__':
    main()