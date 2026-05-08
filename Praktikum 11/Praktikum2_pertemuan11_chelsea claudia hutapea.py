#nama: chelsea claudia hutapea 
#nim: J0403251067
#pertemuan 11

#membuat adjacency list
graph = {
    "A": ["B", "C"], # A terhubung ke B dan C 
    "B": ["A", "D"], # B terhubung ke A dan D
    "C": ["A", "D"], # C terhubung ke A dan D
    "D": ["B", "C"]  # D terhubung ke B dan C
}
print("Adjacency List:\n") #menampilkan adjacency list
for node in graph: #manmpilkan setiap node dan tetangganya
    print(node, "->", graph[node])