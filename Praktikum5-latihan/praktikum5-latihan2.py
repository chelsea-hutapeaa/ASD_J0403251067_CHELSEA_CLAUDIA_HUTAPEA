#====================================
#Latihan 2 : Tracking Rekursi 
#====================================

def countdown(n):
    #base case
    if n == 0:
        print("selesai")
        return
    
    print("masuk: {n}") #menampilkan nilai n saat masuk ke fungsi
    countdown(n - 1) #rekursi dengan n yang lebih kecil
    print("keluar: {n}") #menampilkan nilai n saat keluar dari fungsi

countdown(3)