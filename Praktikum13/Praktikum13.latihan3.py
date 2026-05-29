# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Menggunakan heapq untuk priority queue
import heapq
# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}
# Fungsi algoritma Prim
def prim(graph, start):
    # Menyimpan node yang sudah dikunjungi
    visited = set([start])
    # Priority queue untuk edge
    edges = []
    # Memasukkan seluruh edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    # Menyimpan MST
    mst = []
    # Menyimpan total bobot
    total_weight = 0
    # Selama masih ada edge
    while edges:
        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)
        # Jika node tujuan belum dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            # Menambahkan edge baru ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight
# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot
print("Total bobot =", total)


# ==========================================================
# Soal Analisis
# ==========================================================
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
# ==========================================================
# Jawaban Analisis
# ==========================================================
# 1. Node awal yang digunakan adalah A.
# 2. Edge pertama yang dipilih adalah A-C dengan bobot 2.
# 3. Prim memilih edge dengan bobot paling kecil yang menghubungkan node yang sudah ada di MST dengan node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Perbedaan Prim dan Kruskal:
#    - Prim membangun tree mulai dari satu node awal.
#    - Kruskal memilih edge terkecil secara global.