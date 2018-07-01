from mpi4py import MPI
import math
import time
start = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
SENHA = "999999"

if rank == 0:
    i = 1
    # Fica recebendo mensagens das threads para saber qual achou a senha
    while True:
        recv = comm.recv(source=i)
        if recv['PasswordFound']: break

        if i < size-1: i += 1
        else: i = 1

    print("Thread " + str(i) + " found password")

else:
    size -= 1
    rank -= 1
    words = [w.strip() for w in open("wordlist3.txt", "r").readlines()]
    n = len(words)
    m = math.ceil(n / size)

    if rank == size-1: search_range = range(m * rank, n)
    else: search_range = range( m*rank, (m*rank) + m )

    data = {'PasswordFound': False, 'Password': ''}
    for i in search_range:
        if SENHA == words[i]:
            data['PasswordFound'] = True
            data['Password'] = words[i]
            comm.send(data, dest=0)

            tempo_execucao = time.time() - start
            print("Tempo de Execução: ", tempo_execucao)

            break

        comm.send(data, dest=0)