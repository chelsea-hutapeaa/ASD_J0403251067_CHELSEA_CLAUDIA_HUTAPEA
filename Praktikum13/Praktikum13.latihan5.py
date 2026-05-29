# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Data jalan antar kota
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()
mst = []
total_weight = 0
connected = set()
# Proses Kruskal
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
# Menampilkan MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
# Menampilkan total bobot
print("Total Bobot =", total_weight)


# ==========================================================
# Soal Analisis
# ==========================================================
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?
# ==========================================================
# Jawaban Analisis
# ==========================================================
# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih:
#    Bogor-Depok = 2
#    Depok-Jakarta = 3
#    Depok-Bandung = 4
# 4. Total bobot MST: 2 + 3 + 4 = 9
# 5. Edge Bogor-Jakarta dan Jakarta-Bandung tidak dipilih karena terdapat jalur lain dengan bobot lebih kecil sehingga biaya total menjadi minimum.