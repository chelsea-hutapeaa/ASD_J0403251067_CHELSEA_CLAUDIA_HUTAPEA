#nama: chelsea claudia hutapea 
#nim: J0403251067
#pertemuan 11

# membuat adjacency matrix
nodes = [0, 1, 2, 3]
matrix = [
    [0, 1, 1, 0],  # Node 0 terhubung dengan Node 1 dan Node 2
    [1, 0, 1, 0], # Node 1 terhubung dengan Node 0 dan Node 2
    [1, 1, 0, 1], # Node 2 terhubung dengan Node 0, Node 1, dan Node 3
    [0, 0, 1, 0]  # Node 3 terhubung dengan Node 2
]
print("Adjacency Matrix:\n")
for row in matrix:
    print(row)
print("\n penjelasan setiap baris:")
for i in range(len(matrix)):
    print(f"baris {i}: {matrix[i]}")