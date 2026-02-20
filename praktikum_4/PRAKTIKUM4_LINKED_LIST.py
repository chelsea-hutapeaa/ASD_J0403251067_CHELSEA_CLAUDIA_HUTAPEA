#=============================================
#NAMA : CHELSEA CLAUDIA HUTAPEA
#NIM : J0403251067
#KELAS : TPL A1
#=============================================

#============================================
#Implementasi Dasar : Node pada Linked list
#============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data  #menyimpan data pada node
        self.next = None  #pointer untuk menunjuk ke node berikutnya, default None

#1) membuat node dengan instantiasi class node 
nodeA = Node("A")  
nodeB = Node("B") 
nodeC = Node("C")

#2) mendefinisikan head dan menghubungkan Node : A -> B -> C -> None
head = nodeA  
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri node dari head samapai ke none 
current = head  
while current is not None:  
    print(current.data)  #menampilkan data pada node saat ini
    current = current.next  #pindah ke node berikutnya 

#============================================
#Implementasi Dasar : Stack 
#============================================

