#=========================================
#Praktikum 1 : konsep ADT dan FILE handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#=========================================


print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))

print("====Membuka file per baris====")
jumlah_baris = 0 #inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke-:", jumlah_baris)
        print("isinya :", baris)

#=====================================================================
#Praktikum 1 : konsep ADT dan FILE handling
#Latihan Dasar 2 : Membaca data dan menyimpannya ke struktur data list
#=====================================================================    
#parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM   :", nim, " |Nama :", nama, " |Nilai :", nilai) #menampilkan satuan data dalam bentuk kolom

#=========================================
#Praktikum 1 : konsep ADT dan FILE handling
#Latihan Dasar 3 : Membaca data dan menyimpannya dalam list
#=========================================

data_list = [] #inisialisasi list untuk menampung data 
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append( (nim, nama, int(nilai)) ) #simpan data ke list
print("===menampilkan list====")
print(data_list)
print("contoh record ke 1", data_list[0]) 
print("contoh record ke 2", data_list[1])
print("jumlsh record pada list :", len(data_list))

#=========================================
#Praktikum 1 : konsep ADT dan FILE handling
#Latihan Dasar 4 : Membaca data dan menyimpannya dalam dictionary 
#=========================================
data_dict = {} #inisialisasi dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary (key: nim, value: nama, nilai)
        data_dict[nim] = {
            "nama": nama, 
            "nilai": int(nilai)
        }
print("===menampilkan dictionary====")
print(data_dict)