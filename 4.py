# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

nim = int(input("Input 3 digit NIM terakhir : "))

if nim > 0:
    if 1 <= nim <= 50:
        if nim % 2 == 0:
            print("Silahkan masuk ke kelas K2")
        else:
            print("Silahkan masuk ke kelas K1")
    elif 51 <= nim <= 100:
        if nim % 2 == 0:
            print("Silahkan masuk ke kelas K4")
        else:
            print("Silahkan masuk ke kelas K3")
    elif 101 <= nim <= 150:
        if nim % 2 == 0:
            print("Silahkan masuk ke kelas K6")
        else:
            print("Silahkan masuk ke kelas K5")
    else:
        if nim % 2 == 0:
            print("Silahkan masuk ke kelas K8")
        else:
            print("Silahkan masuk ke kelas K7")
else:
    print("Masukkan NIM yang valid!")