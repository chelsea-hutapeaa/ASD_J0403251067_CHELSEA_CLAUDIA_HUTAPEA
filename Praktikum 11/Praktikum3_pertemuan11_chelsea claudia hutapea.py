#nama: chelsea claudia hutapea 
#nim: J0403251067
#pertemuan 11

matrix = [
    [0, 1, 1, 0],  #node 0 terhubung ke 1 dan 2 
    [1, 0, 1, 0],  #node 1 terhubung ke 0 dan 2
    [1, 1, 0, 1],  #node 2 terhubung ke 0, 1, dan 3
    [0, 0, 1, 0]   #node 3 terhubung ke 2
]
nodes = [0, 1, 2, 3] #daftar node 
adjacency_list = {} #dictionary kosong untuk menyimpan tetangga node
for i in range(len(matrix)): #perulangan setiap baris matriks
    neighbors = [] #list kosong untuk menyimpan tetangga node saat ini
    for j in range(len(matrix[i])): #perulangan setiap kolom dalam baris saat ini
        if matrix[i][j] == 1: #jika ada koneksi antara node i dan j
            neighbors.append(j) #tambahkan node j ke daftar tetangga node i
    adjacency_list[nodes[i]] = neighbors #simpan daftar tetangga untuk node saat ini

print("adjacency list:\n") #menampilkan adjacency liat
for node in adjacency_list: #perulangan setiap node dalam adjacency list
    print(node, "->", adjacency_list[node]) #menampilkan node dan tetangganya