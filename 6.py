# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

count = 0
n = int(input("Masukkan nilai N = "))

def is_prima(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(1, n+1):
    num = int(input(f"Masukkan bilangan ke-{i} = "))
    if is_prima(num):
        count += num

if count == 0:
    print("Tidak ada item list yang bilangan prima")
else:
    print(f"Jumlah bilangan prima adalah {count}")