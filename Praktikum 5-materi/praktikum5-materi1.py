#====================================
# contoh rekursi 1 :  Faktorial 
#====================================

def faktorial(n):
    #base case: berhenti ketika n = 0
    if n == 0:
        return 1
    #recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)
print(faktorial(5)) # Output: 120