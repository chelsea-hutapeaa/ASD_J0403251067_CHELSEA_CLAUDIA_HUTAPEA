#====================================
#Latihan 4 : Kombinasi huruf 
#Nama : Chelsea Claudia Hutapea
#NIM : J0403251067
#KELAS : TPL A1
#====================================

def kombinasi(n, hasil=""):
    #membuat semua kombinasi huruf a dan b sepanjang n , untuk n=2 maka semua kemungkinan string sepanjang 2
    #base case: jika panjang string sudah sama dengan n, maka cetak hasil dan hentikan rekursi
    if len(hasil) == n:
        print(hasil)
        return
    
    #recursive case: setiap langkah rekursi menambahkan huruf 'a' atau 'b' ke hasil saat ini, dan memanggil fungsi kombinasi lagi untuk melanjutkan proses pembentukan string
    kombinasi(n, hasil + "A")
    
    kombinasi(n, hasil + "B")

kombinasi(2)