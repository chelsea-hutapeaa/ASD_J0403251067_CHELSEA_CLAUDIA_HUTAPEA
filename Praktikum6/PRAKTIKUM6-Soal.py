#====================================
# NAMA : Chelsea Claudia Hutapea
# NIM : J0403251067 
# KELAS : TPL A1
# Soal
#====================================

# Soal: 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
#Soal 2. Kandidat berapa saja yang lolos?
def quick_sort_nilai(arr):
    helper_sort(arr, 0, len(arr)-1)

def helper_sort(arr, awal, akhir):
    if awal < akhir:
        posisi_pivot = bagi_data(arr, awal, akhir)

        helper_sort(arr, awal, posisi_pivot-1)
        helper_sort(arr, posisi_pivot+1, akhir)

def bagi_data(arr, awal, akhir):
    pivot = arr[awal]

    kiri = awal + 1
    kanan = akhir

    selesai = False
    while not selesai:

        while kiri <= kanan and arr[kiri] >= pivot:
            kiri = kiri + 1

        while kanan >= kiri and arr[kanan] <= pivot:
            kanan = kanan - 1

        if kanan < kiri:
            selesai = True
        else:
            arr[kiri], arr[kanan] = arr[kanan], arr[kiri]

    arr[awal], arr[kanan] = arr[kanan], arr[awal]

    return kanan

skor_pelamar = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

quick_sort_nilai(skor_pelamar)

print("Urutan skor dari tertinggi ke terendah:")
print(skor_pelamar)

top_kandidat = skor_pelamar[:5]

print("\n5 kandidat dengan nilai tertinggi:")
print(top_kandidat)