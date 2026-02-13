#-------------------------
#Pertemuan 3 
#-------------------------

#latihan 3 : implementasikan pencarian pada node tertentu Double Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
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
        new_node.prev = temp

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

dll = DoublyLinkedList()
data_list = [2, 6, 9, 14, 20]
print("Masukkan elemen ke dalam Doubly Linked List:", ", ".join(map(str, data_list)))

for data in data_list:
    dll.append(data)

key = int(input("Masukkan elemen yang ingin dicari: "))
if dll.search(key):
    print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")