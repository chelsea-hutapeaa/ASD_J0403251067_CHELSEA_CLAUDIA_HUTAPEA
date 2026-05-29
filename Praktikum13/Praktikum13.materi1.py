# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# Materi 1 : Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node_asal, node_tujuan)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan seluruh edge berdasarkan bobot terkecil
# Kruskal selalu memilih bobot terkecil terlebih dahulu
edges.sort()

# Menyimpan edge yang terpilih ke MST
mst = []
# Menyimpan total bobot MST
total_weight = 0
# Menyimpan node yang sudah terhubung
connected = set()
# Memproses seluruh edge yang sudah diurutkan
for weight, u, v in edges:
    # Memastikan edge yang dipilih tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # Menambahkan edge ke MST
        mst.append((u, v, weight))
        # Menambahkan bobot ke total MST
        total_weight += weight
        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot MST
print("Total bobot =", total_weight)

# ==========================================================
# Penjelasan Materi
# ==========================================================

# Algoritma Kruskal bekerja dengan cara:
# 1. Mengurutkan seluruh edge berdasarkan bobot terkecil.
# 2. Memilih edge satu per satu mulai dari bobot terkecil.
# 3. Edge hanya dipilih jika tidak membentuk cycle.
# 4. Proses berhenti ketika seluruh node sudah terhubung.
