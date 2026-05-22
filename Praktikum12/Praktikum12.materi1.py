# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Pertemuan 12 - 22 Mei 2026
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

import heapq

# Graph berbobot
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak tercepat ke setiap node
    distances = {node: float('inf') for node in graph}
    # Node awal memiliki jarak 0
    distances[start] = 0
    # Priority queue untuk memilih jarak terkecil
    pq = [(0, start)]
    while pq:
        # Mengambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq)
        # Mengecek semua tetangga node
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru
            distance = current_distance + weight
            # Jika jarak lebih kecil, update data
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, 'A')
# Menampilkan hasil
print("Hasil shortest path:")
print(hasil)

