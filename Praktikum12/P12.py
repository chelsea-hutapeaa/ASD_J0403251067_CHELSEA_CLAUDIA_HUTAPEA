# NAMA: CHELSEA CLAUDIA HUTAPEA
# NIM: J0403251067
# KELAS: A1 
#PERTEMUAN 12 22 MEI 2026

# ==========================================
# Menghitung biaya untuk mencapai node
# ==========================================

# Weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'C': {'B': 1},
    'B': {}
}

biaya_langsung = graph['A']['B'] # Biaya langsung A -> B
biaya_melalui_c = graph['A']['C'] + graph['C']['B']# Biaya melalui C
# Menampilkan hasil
print("Biaya A -> B =", biaya_langsung)
print("Biaya A -> C -> B =", biaya_melalui_c)
# Menentukan biaya terkecil
if biaya_langsung < biaya_melalui_c:
    print("Biaya paling kecil =", biaya_langsung)
    print("Jalur terbaik: A -> B")
else:
    print("Biaya paling kecil =", biaya_melalui_c)
    print("Jalur terbaik: A -> C -> B")