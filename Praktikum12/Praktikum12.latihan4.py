# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}# Semua jarak awal dibuat tak hingga
    distances[start] = 0    # Node awal bernilai 0

    priority_queue = [(0, start)]    # Priority queue

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:        # Jika jarak lebih besar, lewati
            continue
        for neighbor, weight in graph[current_node].items():        # Memeriksa semua tetangga
            distance = current_distance + weight            # Menghitung jarak baru

            if distance < distances[neighbor]:            # Jika ditemukan jarak lebih kecil
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menjalankan Dijkstra
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil
print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Soal Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin
#    dengan waktu tempuh 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah:
#    Gerbang -> Kantin -> Lab -> Aula
#    Total = 2 + 4 + 1 = 7 menit
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil
#    karena bisa saja terdapat jalur lain dengan lebih banyak
#    edge tetapi total bobotnya lebih kecil.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini
#    karena semua bobot bernilai positif dan algoritma dapat
#    mencari jalur tercepat secara efisien.
# ==========================================================