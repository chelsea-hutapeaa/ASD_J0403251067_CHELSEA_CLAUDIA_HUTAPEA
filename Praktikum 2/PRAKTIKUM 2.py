#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 1 : membuat fungsi load data dari file 
#===========

#variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item
            nim = nim.strip()  # hilangkan spasi di nim
            nama = nama.strip()  # hilangkan spasi di nama
            nilai = nilai.strip()  # hilangkan spasi di nilai
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} #masukkan dalam 
    return data_dict

buka_data = baca_data(nama_file)
print ("jumlah data terbaca ", len(buka_data)) # melihat berapa data yang di load


#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 2 : membuat fungsi menampilkan data
#===========

def tampil_data(data_dict):
    #membuat header tabel
    print("\n========DAFTAR MAHASISWA========")
    print(f"{'NIM':<10} | {'NAMA':<20} | {'NILAI':<5}")
    print("-" * 40) # membuat garis 
    
    # menampilkan isi datanya 
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} | {nama:<20} | {nilai:<5}")
    
tampil_data(buka_data) #memanggil fungsi tampil data

#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 3 : membuat fungsi mencari data
#===========

# membuat fungsi pencarian data 
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary 
    #membuat input nim mahasiswa akan dicari 
    nim_cari = input("Masukkan NIM mahasiswa yang dicari : ").strip()

    if nim_cari in data_dict: 
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']

        print("======Data ditemukan=====:")
        print(f"NIM   : {nim_cari}")
        print(f"NAMA  : {nama}")
        print(f"NILAI : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar.")

#memanggil fungsi cari data 
#cari_data(buka_data)


#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 4 : membuat fungsi update data
#===========

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukkan NIM mahasiswa yang ingin di ubah datanya : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. update dibatalkan.")
        return
    

    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 :").strip())
    except ValueError:
        print("Nilai harus berupa angka. update dibatalkan.")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. update dibatalkan.")
        return
    

    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")
    # otomatis simpan perubahan ke file
    try:
        simpan_data(data_dict, nama_file)
    except Exception:
        print("Gagal menyimpan otomatis. Silakan pilih menu 4 untuk menyimpan.")

#memanggil fungsi ubah data
#ubah_data(buka_data)

#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 5 : membuat fungsi menyimpan data pada file 
#===========

#membuat fungsi menyimpan data ke file 
def simpan_data(data_dict, nama_file):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")
    print("Data berhasil disimpan ke file.")

# panggil simpan data setelah ubah data
#simpan_data(buka_data, nama_file)
#print("\nData berhasil disimpan ke file:", nama_file)


#===========
# praktikum 2 : konsep ADT dan FILE handling (studi kasus)
# latihan 6 : membuat fungsi menyimpan data pada file 
#===========

def main():
    #load data otomatis saat program di mulai
    buka_data = baca_data(nama_file) #fs. fungsi load data dari 

    while True:
        print("\n===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu : ").strip()

        if pilihan == '1':
            tampil_data(buka_data)

        elif pilihan == '2':
            cari_data(buka_data)

        elif pilihan == '3':
            ubah_data(buka_data)

        elif pilihan == '4':
            simpan_data(buka_data, nama_file)

        elif pilihan == '0':
            print("program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()