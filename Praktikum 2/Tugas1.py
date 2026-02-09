#======================================
# TUGAS HANDS-ON MODUL 1 
# Studi kasus: Sistem kasus stok barang kantin (berbasis file .txt)
#
#Nama : Chelsea Claudia Hutapea
#NIM  : J0403251067
#Kelas: TPLA1
#======================================

#--------------------------------------
# KONSTANTA NAMA FILE 
#--------------------------------------
Nama_file = "stok_barang.txt"

#--------------------------------------
# fungsi membaca data dari file 
#--------------------------------------
def baca_data(nama_file):
    """
    Membaca data dari file teks.
    format per baris: kodebarang, namabarang, stok
    output:
    - stock_dict (dictionary)
      key   = kode_barang
      value = {"nama": nama_barang, "stok": stok_int}
    """
    stock_dict = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file: #loop untuk setiap baris dalam file
            baris = baris.strip() #ambil data per baris dan hilangkan karakter newline
            kodebarang, namabarang, stokbarang = baris.split(',')#ambil data per item data 
            stock_dict[kodebarang] = {"nama barang": namabarang, "stok barang": int(stokbarang)} #masukkan dalam dictionary
    return stock_dict
buka_data = baca_data(Nama_file) #memanggil fungsi load data dan menyimpan dalam variabel buka_data
# TODO: Untuk setiap baris:
# - gunakan strip() untuk menghilangkan \n
# - split(",") untuk memisahkan kolom
# - simpan ke dictionary

#--------------------------------------
# FUNGSI : Menyimpan data ke file
#--------------------------------------
def simpan_data(nama_file, stock_dict):
    """
    Menyimpan seluruh data stock ke file teks.
    format per baris: kodebarang, namabarang, stok
    """
    with open(nama_file, 'w', encoding='utf-8') as file:
        for kodebarang in sorted(stock_dict.keys()): #loop untuk setiap kode barang yang tersimpan
            namabarang = stock_dict[kodebarang]["nama barang"]#mengambil nama barang dari dictionary
            stokbarang = stock_dict[kodebarang]["stok barang"]#mengambil stok barang dari dictionary
            file.write(f"{kodebarang}, {namabarang}, {stokbarang}\n")#tulis ke file dalam format yang sesuai
            
        # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
        # Hint: with open(nama_file, "w", encoding="utf-8") as f:

        print("data berhasil disimpan ke file:", nama_file) #konfirmasi penyimpanan 
        pass

#--------------------------------------
# fungsi menampilkan semua data 
#--------------------------------------
def tampilkan_data(stock_dict):
    """
    menampilkan semua barang di stok_dict.
    """
    print("\n==============DAFTAR STOK BARANG==============")
    print(f"{'kode barang' : <10} {'nama barang' : <12} {'stok barang' : >5}")

    # TODO: Jika kosong, tampilkan pesan stok kosong
    # TODO: Tampilkan dengan format rapi: kode | nama | stok 

    print("-" * 32)#membuat garis 

    #menampilkan isi datanya 
    for kodebarang in sorted(stock_dict.keys()): #loop untuk setiap kode barang yang tersimpan
        namabarang = stock_dict[kodebarang]["nama barang"]#mengambil nama barang dari dictionary
        stokbarang = stock_dict[kodebarang]["stok barang"]#mengambil stok barang dari dictionary
        #tampilkan dalam format tabel 
        print(f"{kodebarang : <10} | {namabarang : <12} | {int(stokbarang) : >5}")#menampilkan data dalam format yang sesuai


#--------------------------------------
# fungsi: cari barang berdasarkan kode
#--------------------------------------
def cari_barang(stock_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode_cari = input("Masukkan kode barang yang dicari:").strip() #meminta input kode barang yang dicari

    if kode_cari in stock_dict: #cek kode barang apakah ada dalam dictionary
        namabarang = stock_dict[kode_cari]["nama barang"]#mengambil nama barang dari dictionary
        stokbarang = stock_dict[kode_cari]["stok barang"]#mengambil stok barang dari dictionary
        #tampilkan hasil pencarian
        print("=========Data Barang ditemukan=========")#tampikan detail barang
        print(f"Kode Barang : {kode_cari}") #tampilkan kode barang
        print(f"Nama Barang : {namabarang}") #tampilkan nama barang
        print(f"Stok Barang : {stokbarang}") #tampilkan stok barang
    else:
        print("Barang dengan kode tersebut tidak ditemukan.") #tampilkan pesan jika barang tidak ditemukan
    # TODO: Cek apakah kode ada di dictionary
    # Jika ada: tampilkan detail barang
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'

    pass


#--------------------------------------
# fungsi: tambah barang baru
#--------------------------------------

def tambah_barang(stock_dict):
    kodebarang = input("Masukkan kode barang baru: ").strip() #meminta input kode barang baru

    #memvalidasi bahwa tidak boleh ter duplikat 
    if kodebarang in stock_dict: #cek apakah kode barang sudah ada
        print("Kode barang sudah ada dalam stok.") #tampilkan pesan jika kode barang sudah ada
        return  #kembalikan dictionary tanpa perubahan

    namabarang = input("Masukkan nama barang baru: ").strip() #meminta input nama barang baru

    #input stok awal
    try:
        stok_awal = int(input("Masukkan stok awal barang (harus angka): ")) #meminta input stok awal barang baru
        if stok_awal < 0: #cek stok tidak boleh kosong 
            print("Stok awal tidak boleh negatif.") #tampilkan pesan jika stok awal negatif
            return  #kembalikan dictionary tanpa perubahan
    except ValueError: #jika input bukan angka 
        print("Input tidak valid. Stok awal harus berupa angka.") #tampilkan pesan jika stok awal bukan angka
        return  #kembalikan dictionary tanpa perubahan
    
    #menyimpan data barang baru ke dictionary
    stock_dict[kodebarang] = {"nama barang": namabarang, "stok barang": stok_awal} #simpan data barang baru ke dictionary
    print(f"Barang baru '{namabarang}' berhasil ditambahkan dengan stok {stok_awal}.") #tampilkan pesan konfirmasi penambahan barang baru


#--------------------------------------
# fungsi: update stok barang
#--------------------------------------

def update_stok(stock_dict):
    '''
    mengubah stok barang (tambah atau kurangi).
    stok tidak boleh menjadi negatif.
    '''
    kode = input("Masukkan kode barang yang akan diupdate stoknya: ").strip() #meminta input kode barang yang akan diupdate

    #mengecek apakah kode barang ada dalam dictionary
    if kode not in stock_dict: #cek apakah kode barang tidak ada
        print(f"Barang dengan kode '{kode}' tidak ditemukan.") #tampilkan pesan jika barang tidak ditemukan
        return  #kembalikan dictionary tanpa perubahan
    print(f"Barang ditemukan: {stock_dict[kode]['nama barang']}") #tampilkan nama barang yang ditemukan
    print(f"Stok saat ini: {stock_dict[kode]['stok barang']}") #tampilkan detail barang yang ditemukan

    print("\npiliha jenis update:")#pilihan jenis update
    print("1. Tambah stok")#opsi tambah stok
    print("2. Kurangi stok")#opsi kurangi stok

    pilihan = input("Masukkan pilihan (1/2): ").strip() #meminta input pilihan jenis update

    #menginput jumlah perubahan stok barang
    try: # mengubah input menjadi integer
        jumlah = int(input("Masukkan jumlah stok yang akan diubah: ")) #meminta input jumlah perubahan stok
        if jumlah < 0: #cek jumlah tidak boleh negatif
            print("Jumlah tidak boleh negatif.") #tampilkan pesan jika jumlah negatif
            return  #kembalikan dictionary tanpa perubahan
        
    except ValueError: #jika input bukan angka
        print("Input tidak valid. Jumlah harus berupa angka.") #tampilkan pesan jika jumlah bukan angka
        return  #kembalikan dictionary tanpa perubahan
    
    stok_sekarang = stock_dict[kode]['stok barang'] #mengambil stok barang saat ini dari dictionary

    if pilihan == '1':  #jika pilihan tambah stok
        stok_baru = stok_sekarang + jumlah #menghitung stok baru
        stock_dict[kode]['stok barang'] = stok_baru #update stok barang dalam dictionary
        print(f"Stok barang '{stock_dict[kode]['nama barang']}' berhasil ditambah. Stok baru: {stock_dict[kode]['stok barang']}") #tampilkan pesan konfirmasi penambahan stok

    elif pilihan == '2':  #jika pilihan kurangi stok 
        stok_baru = stok_sekarang - jumlah #menghitung stok baru
        if stok_baru < 0: #cek stok baru tidak boleh negatif
            print("Stok tidak boleh menjadi negatif. Operasi dibatalkan.") #tampilkan pesan jika stok baru negatif
        else:
            stock_dict[kode]['stok barang'] = stok_baru #update stok barang dalam dictionary
            print(f"Stok barang '{stock_dict[kode]['nama barang']}' berhasil dikurangi. Stok baru: {stock_dict[kode]['stok barang']}") #tampilkan pesan konfirmasi pengurangan stok
    else: #jika pilihan tidak valid
        print("Pilihan tidak valid. Operasi dibatalkan.") #tampilkan pesan jika pilihan tidak valid


#--------------------------------------
# PROGRAM UTAMA
#--------------------------------------

def main():
    #membaca data dari file saat program dimulai
    buka_data = baca_data(Nama_file)

    while True: #loop menu sampai user keluar 
        print("\n=====MENU STOK KANTIN=====")#tampilkan menu utama
        print("1. Tampilkan semua stok barang")#pilihan menu tampilkan semua stok barang
        print("2. Cari barang berdasarkan kode")#pilihan menu cari barang berdasarkan kode
        print("3. Tambah barang baru")#pilihan menu tambah barang baru
        print("4. Update stok barang")#pilihan menu update stok barang
        print("5. Simpan data ke file")#pilihan menu simpan data ke file
        print("0. Keluar")#pilihan menu keluar program
        
        pilihan = input("Masukkan pilihan Anda (0-5): ").strip() #meminta input pilihan menu

        if pilihan == '1': #jika pillihan 1
            tampilkan_data(buka_data)  #tampilkan semua data stok barang

        elif pilihan == '2': #jika pilihan 2
            cari_barang(buka_data)  #memanggil fungsi cari barang

        elif pilihan == '3': #jika pilihan 3
            tambah_barang(buka_data)  #tambah barang baru
            
        elif pilihan == '4': #jika pilihan 4
            update_stok(buka_data)  #update stok barang

        elif pilihan == '5': #jika pilihan 5
            simpan_data(Nama_file, buka_data)  #simpan data ke file
            print("Data telah disimpan ke file.") #tampilkan pesan konfirmasi penyimpanan

        elif pilihan == '0': #jika pilihan 0
            print("Keluar dari program. Sampai jumpa!") #tampilkan pesan keluar
            break  #keluar dari loop menu

        else: #jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan coba lagi.") #tampilkan pesan jika pilihan tidak valid

    #menjalankan program utama 
if __name__ == "__main__":
    main()