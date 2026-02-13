#-------------------------
#Pertemuan 3 
#-------------------------

#latihan 5 : Menambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    def reverse(self):
        prev = None
        current = self.head
        next_node = None

        while current:
            next_node = current.next   
            current.next = prev        
            prev = current             
            current = next_node        
        self.head = prev               

ll = LinkedList()
data_input = input("Masukkan elemen untuk Linked List: ")
data_list = list(map(int, data_input.split(",")))

for data in data_list:
    ll.append(data)
print("Linked List sebelum dibalik:", end=" ")
ll.display()
ll.reverse()
print("Linked List setelah dibalik:", end=" ")
ll.display()