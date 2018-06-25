import sys
from mpi4py import MPI
import numpy

G_usuario = "Teste"
G_senha = "0001"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def brute(usuario, senha):
    if G_usuario == usuario:
        if G_senha == senha:
            print("Senha encontrada: ", senha)
            return True
        else:
            print("Tentantiva falha: ", senha)
            return False

def main():
    words = [w.strip() for w in open("wordlist_test.txt", "r").readlines()]
    print("Eu sou o core " + str(rank))

    if rank == 0:
        print("Entrando no core 0")
        data = "Senha encontrada no core 0"
        for i in range(0, len(words)//2):
            req = comm.irecv(source=1, tag=11)
            data = req.wait()
            print("Core 0 ta dizendo que recebeu um ok do core 1")
            print(str(data))

            find_password = brute(G_usuario, words[i])
            if find_password:
                comm.isend(data, dest=1, tag=11)
                print(data)
            else: print('Not found on core 0')


    elif rank == 1:
        data = "Senha encontrada no core 1"

        for i in range(len(words)//2 - 1, len(words)):
            req = comm.irecv(source=0, tag=11)
            data = req.wait()
            print("Core 1 ta dizendo que recebeu um ok do core 0")
            print(str(data))

            find_password = brute(G_usuario, words[i])
            if find_password:
                comm.isend(data, dest=0, tag=11)
                print(data)
            else: print('Not found on core 1')


if __name__ == '__main__':
    main()