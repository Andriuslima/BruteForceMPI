from mpi4py import MPI

# EXECUTE = mpiexec -n 3 python brute_force.py

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

### MPI TESTS ###

# non blocking communation
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print("Sending data from 0")
    req = comm.isend(data, dest=1, tag=11)
    req.wait()
    print("Data send from 0")
elif rank == 1:
    print("Receiving data on 1")
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print("Data received on 0:" + str(data))

"""
## Point-to-point communation. Sending data from process 0 to process 1
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print("I'm ranked 1 and I recieved this data: " + str(data))


# NumPy array --> fast way
# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(1000, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    data = numpy.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)

# automatic MPI datatype discovery
if rank == 0:
    data = numpy.arange(100, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = numpy.empty(100, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)


## Collective Communication -> Broadcast
# http://mpi4py.scipy.org/docs/usrman/tutorial.html
"""