#====================================
#Latihan 5 : generator pin
#Nama : Chelsea Claudia Hutapea
#NIM : J0403251067
#KELAS : TPL A1
#====================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print(hasil)
        return
    
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)