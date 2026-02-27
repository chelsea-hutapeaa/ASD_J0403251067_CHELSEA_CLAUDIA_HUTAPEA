#====================================
#Latihan 3 : Mencari nilai maksimum
#Nama : Chelsea Claudia Hutapea
#NIM : J0403251067
#KELAS : TPL A1
#====================================

def cari_maks(data, indeks=0):
    #base case
    if indeks == len(data) - 1:
        return data[indeks]
    #recursive case
    maks_sisa = cari_maks(data, indeks + 1)

    if data[indeks] > maks_sisa:
        return data[indeks]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("nilai maksimum:", cari_maks(angka))