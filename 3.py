# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

n = int(input("Berapa kali ingin bernyanyi: "))
count = n

for i in range(n):
    print(f"{count} bebek kecil berenang")
    print("Menyusuri sungai yang deras")
    print("Induknya mencari kwek kwek kwek")
    if not (count == 1):
        print(f"Hanya {count-1} ekor yang pulang\n")
        count -= 1
        continue
    print("Dan semua bebek kecil pulang, aha!")
    