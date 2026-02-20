#=============================================
#NAMA : CHELSEA CLAUDIA HUTAPEA
#NIM : J0403251067
#KELAS : TPL A1
#=============================================


#============================================
#Implementasi Dasar : Stack 
#============================================


class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  #menyimpan data pada node
        self.next = None  #pointer untuk menunjuk ke node berikutnya (awal=none)

#stack ada operasi push (memasukkan head baru) dan pop (menghapus head)

class Stack:
    def __init__(self):
        self.top = None  #top menunujuk ke node paling atas (awalnya kosong)
    
    def push(self, data):
        #1 membuat node baru 
        node_Baru = Node(data)  

        #2 node baru menunjuk ke tp yang lama(head lama)
        node_Baru.next = self.top  

        #3 top berpindah ke node baru
        self.top = node_Baru

    def is_empty(self):
        return self.top is None  #stack kosong jika top none 

    def pop(self): #mengambil/menghapus node paling atas (top)
        if self.is_empty():  
            print("Stack kosong, tidak bisa pop")
            return None 
    
        data_terhapus = self.top.data  #soroti bagian top dan simpan di variabel 
        self.top = self.top.next  
        return data_terhapus  #kembalikan data yang dihapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top.data  

    def tampilkan(self):
        current = self.top
        print ("Top -> ", end=" ")  
        while current is not None:  
            print(current.data, end=" -> ")  
            current = current.next  
        print("None")  

#Instantiasi class stack 
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("peek (lihat top):", s.peek())
s.pop()
s.tampilkan()
print("peek (lihat top):", s.peek())