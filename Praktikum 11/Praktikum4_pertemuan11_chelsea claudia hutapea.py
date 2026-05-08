# nama: chelsea claudia hutapea 
#nim:  J0403251067
#pertemuan 11 
#praktikum 4


# ==========================================
# STUDI KASUS GRAPH PETA KOTA
# ==========================================

# Membuat daftar node/kota
nodes = ["Depok", "Bekasi", "Karawang", "Tangerang", "Serang"]

# ==========================================
# ADJACENCY LIST
# ==========================================

# Membuat adjacency list menggunakan dictionary
graph = {

    # Depok terhubung ke Bekasi dan Tangerang
    "Depok": ["Bekasi", "Tangerang"],

    # Bekasi terhubung ke Depok, Karawang, dan Serang
    "Bekasi": ["Depok", "Karawang", "Serang"],

    # Karawang terhubung ke Bekasi dan Serang
    "Karawang": ["Bekasi", "Serang"],

    # Tangerang terhubung ke Depok dan Serang
    "Tangerang": ["Depok", "Serang"],

    # Serang terhubung ke Bekasi, Karawang, dan Tangerang
    "Serang": ["Bekasi", "Karawang", "Tangerang"]
}

# ==========================================
# MENAMPILKAN ADJACENCY LIST
# ==========================================

# Menampilkan judul output
print("==================================")
print("      ADJACENCY LIST")
print("==================================\n")

# Perulangan untuk menampilkan node dan tetangga
for node in graph:

    # Menampilkan isi adjacency list
    print(node, "->", graph[node])

# ==========================================
# ADJACENCY MATRIX
# ==========================================

# Membuat adjacency matrix
matrix = [

# D  B  K  T  S

  [0, 1, 0, 1, 0],  # Depok terhubung ke Bekasi dan Tangerang

  [1, 0, 1, 0, 1],  # Bekasi terhubung ke Depok, Karawang, dan Serang

  [0, 1, 0, 0, 1],  # Karawang terhubung ke Bekasi dan Serang

  [1, 0, 0, 0, 1],  # Tangerang terhubung ke Depok dan Serang

  [0, 1, 1, 1, 0]   # Serang terhubung ke Bekasi, Karawang, dan Tangerang
]

# ==========================================
# MENAMPILKAN ADJACENCY MATRIX
# ==========================================

# Menampilkan judul output
print("\n==================================")
print("      ADJACENCY MATRIX")
print("==================================\n")

# Perulangan untuk menampilkan matrix
for row in matrix:

    # Menampilkan setiap baris matrix
    print(row)

# ==========================================
# MENAMPILKAN NAMA NODE
# ==========================================

# Menampilkan judul
print("\n==================================")
print("          NAMA NODE")
print("==================================\n")

# Perulangan menampilkan node
for node in nodes:

    # Menampilkan nama kota
    print("-", node)

# ==========================================
# MENAMPILKAN HUBUNGAN ANTAR NODE
# ==========================================

# Menampilkan judul
print("\n==================================")
print("     HUBUNGAN ANTAR NODE")
print("==================================\n")

# Menampilkan hubungan antar kota
print("1. Depok terhubung dengan Bekasi")
print("2. Depok terhubung dengan Tangerang")
print("3. Bekasi terhubung dengan Karawang")
print("4. Bekasi terhubung dengan Serang")
print("5. Karawang terhubung dengan Serang")
print("6. Tangerang terhubung dengan Serang")

# ==========================================
# PENJELASAN NODE DAN EDGE
# ==========================================

# Menampilkan judul
print("\n==================================")
print("      PENJELASAN NODE")
print("==================================\n")

# Menampilkan penjelasan node
print("Node adalah kota pada graph:")

print("1. Depok")
print("2. Bekasi")
print("3. Karawang")
print("4. Tangerang")
print("5. Serang")

# Menampilkan jumlah node
print("\nJumlah node =", len(nodes))

# Menampilkan judul edge
print("\n==================================")
print("      PENJELASAN EDGE")
print("==================================\n")

# Menampilkan penjelasan edge
print("Edge adalah jalan penghubung antar kota.")

# Menampilkan jumlah edge
print("\nJumlah edge = 6")

# ==========================================
# ANALISIS GRAPH
# ==========================================

# Menampilkan judul analisis
print("\n==================================")
print("       ANALISIS GRAPH")
print("==================================\n")

# Menampilkan jenis graph
print("1. Jenis Graph")
print("Graph ini termasuk Undirected Graph")
print("karena hubungan antar kota berlaku dua arah.\n")

# Menampilkan analisis sparse graph
print("2. Dense atau Sparse")
print("Graph termasuk Sparse Graph")
print("karena jumlah edge sedikit dibanding")
print("jumlah kemungkinan edge maksimum.\n")

# Menampilkan representasi graph yang cocok
print("3. Representasi yang Lebih Cocok")
print("Adjacency List lebih cocok digunakan")
print("karena lebih hemat memori.\n")

# ==========================================
# KESIMPULAN
# ==========================================

# Menampilkan judul kesimpulan
print("==================================")
print("          KESIMPULAN")
print("==================================\n")

# Menampilkan kesimpulan
print("Graph digunakan untuk merepresentasikan")
print("hubungan antar kota.")

print("\nKota direpresentasikan sebagai node")
print("dan jalan penghubung direpresentasikan")
print("sebagai edge.")

print("\nAdjacency List lebih cocok digunakan")
print("karena graph yang dibuat termasuk")
print("sparse graph dan lebih hemat memori.")