#-------------------------
#Pertemuan 3 
#-------------------------


#latihan 1 implementasi fungsi untuk menghapus node dengan nilai tertentu.
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data dalam node
        self.next = None  # Menunjuk ke node berikutnya (default: None)

class LinkedList:
    def __init__(self):
        self.head = None  # Head awalnya None, menunjukkan linked list kosong

    # Fungsi untuk menambahkan node baru di akhir linked list
    def append(self, new_data):
        new_node = Node(new_data)  # Membuat node baru dengan data yang diberikan
        if not self.head:  # Jika linked list masih kosong
            self.head = new_node  # Node baru menjadi head
            return
        temp = self.head  # Memulai dari head
        while temp.next:  # Mencari node terakhir dalam linked list
            temp = temp.next
        temp.next = new_node  # Menambahkan node baru di akhir

    # Fungsi untuk menghapus node dengan nilai tertentu
    def delete_node(self, key):
        temp = self.head
        # Jika node pertama adalah node yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next  # Head berpindah ke node berikutnya
            temp = None  # Hapus node pertama
            return
        prev = None
        while temp and temp.data != key:  # Mencari node dengan nilai key
            prev = temp  # Menyimpan referensi ke node sebelumnya
            temp = temp.next
        if temp is None:  # Jika key tidak ditemukan, keluar dari fungsi
            return
        prev.next = temp.next  # Menghapus node dari linked list
        temp = None  # Hapus node dari memori

    # Fungsi untuk mencetak 
    def print_list(self):
        temp = self.head  # Memulai dari head
        while temp:  # Iterasi hingga node terakhir
            print(temp.data, end=" -> ")  # Cetak data
            temp = temp.next  # Pindah ke node berikutnya
        print("None")  # Menunjukkan akhir dari linked list

# Contoh Penggunaan
llist = LinkedList()
llist.append(1)  # Menambahkan node dengan nilai 1
llist.append(2)  # Menambahkan node dengan nilai 2
llist.append(3)  # Menambahkan node dengan nilai 3
llist.append(4)  # Menambahkan node dengan nilai 4

print("Sebelum penghapusan:")
llist.print_list()  # Mencetak linked list sebelum penghapusan

llist.delete_node(3)  # Menghapus node dengan nilai 3

print("Setelah penghapusan:")
llist.print_list()  # Mencetak linked list setelah penghapusan