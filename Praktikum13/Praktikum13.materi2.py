# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# Materi 2 : Algoritma Prim
# ==========================================================

# Mengimpor library heapq
# Digunakan untuk priority queue (min heap)
import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi Prim
def prim(graph, start):
    # Menyimpan node yang sudah dikunjungi
    visited = set([start])
    # Priority queue untuk menyimpan edge
    edges = []
    # Memasukkan seluruh edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(
            edges,
            (weight, start, neighbor)
        )
    # Menyimpan hasil MST
    mst = []
    # Menyimpan total bobot MST
    total_weight = 0
    # Selama masih ada edge dalam priority queue
    while edges:
        # Mengambil edge dengan bobot paling kecil
        weight, u, v = heapq.heappop(edges)
        # Jika node tujuan belum dikunjungi
        if v not in visited:
            # Menandai node sebagai sudah dikunjungi
            visited.add(v)
            # Menambahkan edge ke MST
            mst.append((u, v, weight))
            # Menambahkan bobot ke total MST
            total_weight += weight
            # Menambahkan edge baru dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                # Hanya memasukkan node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(
                        edges,
                        (w, v, neighbor)
                    )

    return mst, total_weight
# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot MST
print("Total bobot =", total)

# ==========================================================
# Penjelasan Materi
# ==========================================================

# Algoritma Prim bekerja dengan cara:
# 1. Memilih satu node awal.
# 2. Mencari edge terkecil dari node yang sudah masuk MST.
# 3. Menambahkan node baru ke MST.
# 4. Mengulangi proses sampai seluruh node terhubung.

# Urutan pemilihan edge:
# A-C = 2
# C-D = 1
# D-B = 3

# Total bobot MST:
# 2 + 1 + 3 = 6

# Perbedaan dengan Kruskal:
# - Kruskal memilih edge global terkecil.
# - Prim membangun tree dari satu node awal.