from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

G_usuario = "Teste"
G_senha = "9999"

words = [w.strip() for w in open("wordlist.txt", "r").readlines()]

def check_pasword(usuario, senha):
    if G_usuario == usuario:
        if G_senha == senha:
            #print("Senha encontrada: ", senha)
            return True
        else:
            #print("Tentantiva falha: ", senha)
            return False


if rank == 0:
    data = {'PasswordFound': False, 'Password': ''}
    for i in range(0, len(words)//2):
        find_password = check_pasword(usuario=G_usuario, senha=words[i])
        if find_password:
            print("Password found on thread 0: " + words[i])
            data['PasswordFound'] = True
            data['Password'] = words[i]

        comm.send(data, dest=1, tag=69)

        data_received = comm.recv(source=1, tag=69)
        if data_received['PasswordFound']:
           print("Thread 1 found password: " + data_received['Password'])
           break

elif rank == 1:
    data = {'PasswordFound': False, 'Password': ''}
    for i in range(len(words)//2 + 1, len(words)):
        find_password = check_pasword(usuario=G_usuario, senha=words[i])
        if find_password:
            print("Password found on thread 1: " + words[i])
            data['PasswordFound'] = True
            data['Password'] = words[i]

        comm.send(data, dest=0, tag=69)

        data_received = comm.recv(source=0, tag=69)
        if data_received['PasswordFound']:
            print("Thread 0 found password: " + data_received['Password'])
            break