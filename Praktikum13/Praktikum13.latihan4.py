# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Implementasi Kruskal
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]
edges.sort()# Mengurutkan berdasarkan bobot

mst = []
total_cost = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_cost += weight
        connected.add(u)
        connected.add(v)
print("Jaringan Kabel Minimum:")
for edge in mst:
    print(edge)
print("Total biaya minimum =", total_cost)

# ==========================================================
# Soal Analisis
# ==========================================================
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini?
# ==========================================================
# Jawaban Analisis
# ==========================================================
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih:
#    GedungC-GedungD = 1
#    GedungA-GedungC = 2
#    GedungB-GedungD = 3
# 3. Total biaya minimum: 1 + 2 + 3 = 6
# 4. MST cocok digunakan karena dapat menghubungkan seluruh gedung dengan biaya pemasangan kabel paling minimum.