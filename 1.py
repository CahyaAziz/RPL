# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

print("Silahkan Login\n")

count = 2

for i in range(3):
    user = input("Username : ")
    password = input("Password : ")
    if user == "loginUTS" and password == "rpl2024":
        print("\nSelamat datang di aplikasi Prodi RPL.")
    else:
        if not(i == 2):
            print(f"\nLogin Salah! Kesempanan anda {count}x lagi.\n")
            count -= 1
            continue
        print("\nAnda tidak diperkenankan mengakses aplikasi ini.")