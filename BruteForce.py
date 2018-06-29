from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
cores = comm.Get_size()
SENHA = "9999"

words = [w.strip() for w in open("wordlist.txt", "r").readlines()]
n = len(words)
m = math.ceil(n/cores)

if rank == cores-1: search_range = range(m*rank, n)
else: search_range = range( m*rank, (m*rank) + m )

data = {'PasswordFound': False, 'Password': ''}
for i in search_range:
    if SENHA == words[i]:
        data['PasswordFound'] = True
        data['Password'] = words[i]
        print("THREAD " + str(rank) + ": found password")