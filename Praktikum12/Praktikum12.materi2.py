# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Representasi weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}    # Semua jarak awal dibuat tak hingga
    distances[start] = 0    # Node awal bernilai 0
    for _ in range(len(graph) - 1):    # Relaksasi edge sebanyak jumlah node - 1
        for node in graph:        # Memeriksa semua edge
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:   # Jika ditemukan jarak lebih kecil
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')# Menjalankan Bellman Ford

# Menampilkan hasil
print("Hasil shortest path:")
print(hasil)