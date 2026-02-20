
#=============================================
#NAMA : CHELSEA CLAUDIA HUTAPEA
#NIM : J0403251067
#KELAS : TPL A1
#=============================================

#============================================
#Implementasi Dasar : Queue
#============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  #menyimpan data pada node
        self.next = None  #pointer untuk menunjuk ke node berikutnya (awal=none)

class Queue:
    #BUAT KONSTRUKTOR UNTUK INISIALISASI FRONT DAN REAR
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None  #node paling belakang

    def is_empty(self):
        return self.front is None  

     #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        NodeBaru = Node(data) 

        #jika queue kosong, front dan rear menunjuk ke node yang sama 
        if self.rear is None:  
            self.front = NodeBaru
            self.rear = NodeBaru
            return

        #jika queue tidak kosong, rear menunjuk ke node baru dan rear berpindah ke node baru    
        self.rear.next = NodeBaru  #letakkan data baru pada setelahnya rear
        self.rear = NodeBaru #jadikan data baru sebagai rear
        
    def dequeue(self):
        #menghapus data dari depan / front
        data_terhapus = self.front.data  

        #geser font ke node berikutnya
        self.front = self.front.next  

        #jika setelah dihapus queue menjadi kosong, rear juga harus di set ke None
        if self.front is None:  
            self.rear = None

        return data_terhapus  
    


    def tampilkan(self):
        current = self.front
        print("Front -> ", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")

#Instantiasi class queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

