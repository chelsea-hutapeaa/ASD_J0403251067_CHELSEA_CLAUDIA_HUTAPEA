# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# ==========================================================

import heapq
# Representasi weighted graph antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}
    # Jarak awal = 0
    distances[start] = 0
    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak lebih besar dari data sebelumnya
        if current_distance > distances[current_node]:
            continue
        # Memeriksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru
            distance = current_distance + weight
            # Jika ditemukan jalur lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ==========================================================
# Soal Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari node awal
#    adalah Depok dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.
# 4. Algoritma Dijkstra bekerja dengan memilih node yang
#    memiliki jarak sementara paling kecil, kemudian
#    memperbarui jarak ke tetangga-tetangganya hingga
#    semua node mendapatkan jarak minimum.
#    Contoh:
#    Bogor -> Depok = 2
#    Depok -> Jakarta = 2
#    Maka:
#    Bogor -> Jakarta = 4
#
#    Jalur menuju Bandung:
#    Bogor -> Depok -> Bandung
#    = 2 + 6
#    = 8
# ==========================================================