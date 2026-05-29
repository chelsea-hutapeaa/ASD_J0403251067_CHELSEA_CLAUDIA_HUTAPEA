# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]
# Mengurutkan edge dari bobot terkecil
edges.sort()
# Menyimpan hasil MST
mst = []
# Menyimpan total bobot MST
total_weight = 0
# Menyimpan node yang sudah terhubung
connected = set()
# Memproses seluruh edge yang sudah diurutkan
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # Menambahkan edge ke MST
        mst.append((u, v, weight))
        # Menambahkan bobot ke total bobot
        total_weight += weight
        # Menandai node sebagai sudah terhubung
        connected.add(u)
        connected.add(v)
# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot
print("Total bobot =", total_weight)


# ==========================================================
# Soal Analisis
# ==========================================================
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih? 
# ==========================================================
# Jawaban Analisis
# ==========================================================
# 1. Edge yang dipilih pertama kali adalah C-D dengan bobot 1.
# 2. Karena algoritma Kruskal selalu memilih edge dengan bobot paling kecil terlebih dahulu untuk memperoleh biaya minimum.
# 3. Total bobot MST yang dihasilkan adalah: 1 + 2 + 3 = 6
# 4. Edge A-B dan A-D tidak dipilih karena seluruh node sudah terhubung sebelum edge tersebut diproses dan pemilihannya dapat membentuk cycle.