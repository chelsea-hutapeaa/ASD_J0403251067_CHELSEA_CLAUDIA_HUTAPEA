#====================================
# NAMA : Chelsea Claudia Hutapea
# NIM : J0403251067 
# KELAS : TPL A1
# Selection Sort Descending
#====================================
def selectionSortDesc(data):
    for i in range(len(data)):
        maxIndex = i

        for j in range(i+1, len(data)):
            if data[j] > data[maxIndex]:
                maxIndex = j

        temp = data[i]
        data[i] = data[maxIndex]
        data[maxIndex] = temp


data = [54,26,93,17,77,31,44,55,20]
selectionSortDesc(data)
print(data)