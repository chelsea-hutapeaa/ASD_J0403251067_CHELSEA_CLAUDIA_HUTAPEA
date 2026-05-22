# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']# Jalur A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']# Jalur A -> C -> D

# Menampilkan hasil perhitungan
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Soal Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9.
#    Perhitungan:
#    A -> B = 4
#    B -> D = 5
#    Total = 4 + 5 = 9
# 2. Total bobot jalur A -> C -> D adalah 3.
#    Perhitungan:
#    A -> C = 2
#    C -> D = 1
#    Total = 2 + 1 = 3
# 3. Jalur yang dipilih sebagai jalur terpendek adalah
#    A -> C -> D karena memiliki total bobot lebih kecil.
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge
#    paling sedikit karena algoritma shortest path fokus pada
#    total bobot terkecil, bukan jumlah langkah perjalanan.
# ==========================================================