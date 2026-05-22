# ==========================================================
# Nama  : Chelsea Claudia Hutapea
# NIM   : J0403251067
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui, dan ditemukan jarak lebih kecil ke neighbor, maka lakukan update jarak
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

# Menjalankan Bellman-Ford
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Soal  Analisis:
# 1. Berapa bobot langsung dari A ke B?
# 2. Berapa total bobot jalur A -> C -> B?
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

# Jawaban Analisis:
#
# 1. Bobot langsung dari A ke B adalah 5.
#
# 2. Total bobot jalur A -> C -> B adalah:
#    4 + (-2) = 2
#
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B
#    adalah A -> C -> B dengan total bobot 2.
#
# 4. Bellman-Ford dapat digunakan pada graph berbobot negatif
#    karena algoritma ini melakukan relaksasi seluruh edge
#    secara berulang sehingga tetap dapat menemukan jarak
#    minimum yang benar.
#
# 5. Relaksasi edge adalah proses memperbarui jarak suatu node
#    jika ditemukan jalur baru yang memiliki total bobot
#    lebih kecil dibanding jarak sebelumnya.
#
# 6. Perbedaan utama Bellman-Ford dan Dijkstra:
#    - Dijkstra lebih cepat tetapi tidak bisa menangani
#      bobot negatif.
#    - Bellman-Ford lebih lambat tetapi bisa menangani
#      bobot negatif.
# ==========================================================