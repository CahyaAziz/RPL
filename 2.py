# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

genap = 0
ganjil = 0

while True:
    num = int(input("Input bilangan : "))
    if num < 0:
        print(f"Jumlah bilangan genap : {genap}")
        print(f"Jumlah bilangan ganjil : {ganjil}")
        break

    if num % 2 == 0:
        genap += num
        continue
    ganjil += num
    