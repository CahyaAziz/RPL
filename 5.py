# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

numBefore = int(input("Input bilangan : "))
count = 0  
loop = 3

while loop > 0:
    numAfter = int(input("Input bilangan : "))
    if numAfter > numBefore:
        count += numAfter
        numBefore = numAfter
        loop = 3
        continue
    numBefore = numAfter
    loop -= 1

print(f"\nHasil penjumlahan nilai yang membesar : {count}")
