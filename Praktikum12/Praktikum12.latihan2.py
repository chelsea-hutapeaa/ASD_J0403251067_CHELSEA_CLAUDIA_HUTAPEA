# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    distances = {node: float('inf') for node in graph}    # Semua jarak awal dibuat tak hingga
    distances[start] = 0    # Jarak dari start ke start adalah 0
    priority_queue = [(0, start)]    # Priority queue menyimpan pasangan (jarak, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari data sebelumnya
        if current_distance > distances[current_node]:
            continue
        # Memeriksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru
            distance = current_distance + weight
            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                # Update jarak
                distances[neighbor] = distance
                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menjalankan algoritma
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Soal Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# 2. Berapa jarak terpendek dari A ke C?
# 3. Berapa jarak terpendek dari A ke D?
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
#    Jalur:
#    A -> C -> D
# 4. Jarak A ke D lebih kecil melalui C karena:
#    A -> C = 2
#    C -> D = 1
#    Total = 3
#    Sedangkan melalui B:
#    A -> B = 4
#    B -> D = 5
#    Total = 9
# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah
#    untuk menyimpan node berdasarkan jarak terkecil sehingga
#    node dengan jarak minimum diproses lebih dahulu.
# 6. Dijkstra tidak cocok untuk graph berbobot negatif karena
#    algoritma ini menggunakan pendekatan greedy dan menganggap
#    jarak minimum yang sudah dipilih tidak akan berubah lagi.
#    Jika ada bobot negatif, hasil shortest path bisa salah.
# ==========================================================