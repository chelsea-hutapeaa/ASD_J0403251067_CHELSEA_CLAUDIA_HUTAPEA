# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
# Seluruh node terhubung dan tidak membentuk cycle
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]
# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)
# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
# Menghitung jumlah edge graph awal
print("\nJumlah edge graph =", len(edges))
# Menghitung jumlah edge spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================================
# soal Analisis
# ==========================================================
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
# ==========================================================
# jawaban Analisis
# ==========================================================
# 1. Graph awal memiliki lebih banyak edge dan dapat memiliki cycle, sedangkan spanning tree hanya menggunakan edge yang diperlukan untuk menghubungkan semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle membuat penggunaan edge menjadi berlebihan dan meningkatkan biaya.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena untuk n node hanya diperlukan n-1 edge agar seluruh node tetap terhubung.