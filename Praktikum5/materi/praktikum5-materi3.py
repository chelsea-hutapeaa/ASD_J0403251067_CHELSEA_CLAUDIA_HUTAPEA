#====================================
#contoh rekursi 3 : Menjumlahkan elemen dalam list 
#====================================

def jumlahkan_list(data, index=0):
    #base case: jika index mencapai panjang list, berhenti
    if index == len(data):
        return 0
    
    #recursive case: jumlahkan elemen saat inni dengan elemen setelahnya 
    return data[index] + jumlahkan_list(data, index + 1)

print(jumlahkan_list([ 2, 4, 6, 8])) # Output: 20