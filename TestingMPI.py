from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data_to_send = {'PasswordFound': True, 'Password': '1234'}
else:
    data_to_send =  {'PasswordFound': False, 'Password': ''}

data = comm.bcast(data_to_send, root=0)

print('rank '+str(rank) + " " + str(data))