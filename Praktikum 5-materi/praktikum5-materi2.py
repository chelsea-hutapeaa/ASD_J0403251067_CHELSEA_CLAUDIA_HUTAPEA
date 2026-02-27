#====================================
#contoh rekursi 2 : Tracking masuk/keluar
#====================================

def hitung(n):
    #base case
    if n == 0:
        print("selesai")
        return
    
    print(f"masuk: {n}") #menampilkan nilai n saat masuk ke fungsi
    hitung(n - 1) #rekursi dengan n yang lebih kecil
    print(f"keluar: {n}") #menampilkan nilai n saat keluar dari fungsi

hitung(3)