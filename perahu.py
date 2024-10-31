def isValid(list):
    source = [["P1", "L1"],["P2", "L2"],["P3", "L3"]]
    tempList = list.copy() # Buat list temporary
    while len(tempList) > 0:
        flag = False
        temp = ["x", "x"] # List untuk membandingkan (idk bro improv 💀)
        for i in tempList:
            temp[0] = i #
            for j in tempList:
                if i == j:
                    continue
                temp[1] = j # Tambahkan 2 nilai dari tempList ke temp
                for n in range(len(source)):
                    if temp[0] == "n": # Jika temp habis maka loop kembali dari awal
                        flag = True
                        break
                    if source[n][0] in temp and source[n][1] in temp: # Jika berpasangan, hapus pasangan dari tempList dan temp
                        temp[0] = "n"
                        temp[1] = "n"
                        tempList.remove(source[n][0])
                        tempList.remove(source[n][1]) 
                if not flag:
                    continue
                break
            if not flag:
                continue
            break
        if not flag:
            allSame = all(item.startswith("P") for item in tempList) or all(item.startswith("L") for item in tempList) # Cek jika semua istri atau semua suami
            if allSame: # Jika semua nilai dalam tempList sama maka VALID, jika ada yang tidak sama maka INVALID
                return True 
            return False
    return True 

def solve(awal, akhir, lokasi_perahu, steps, count):
    if len(awal) == 0: # Jika awal kosong langsung keluar
        return steps
    
    if lokasi_perahu == "left": # Jika "perahu" di kiri
        for i in range(len(awal)):
            for j in range(i + 1, len(awal)):
                p1 = awal[i]
                p2 = awal[j] # Ambil 2 nilai dari awal

                steps.append(f"Sisi awal: {awal}")
                steps.append(f"Sisi Akhir: {akhir}\n")
                steps.append(f"===============[{count}]===============\n")
                awal.remove(p1)
                awal.remove(p2)
                akhir.append(p1)
                akhir.append(p2) # pindahkan dari list awal ke akhir
                
                if isValid(akhir): # Cek jika list akhir valid
                    steps.append(f"{(p1, p2)} Menyebrang\n")
                    count += 1 # steps counter

                    hasil = solve(awal, akhir, "right", steps, count) # rekursi ke perahu kanan
                    if hasil is not None: # Jika hasilnya bukan None (Tidak ada solusi), keluar
                        return hasil
                else:# Jika tidak valid ulangi semua perubahan dan coba lagi
                    awal.append(p1)
                    awal.append(p2)
                    akhir.remove(p1)
                    akhir.remove(p2)
                    steps.pop()
                    steps.pop()
                    steps.pop()
    else: # Jika "perahu" di kanan
        for i in range(len(akhir)):
            p = akhir[i] # Ambil 1 nilai

            steps.append(f"Sisi awal: {awal}")
            steps.append(f"Sisi Akhir: {akhir}\n")
            steps.append(f"===============[{count}]===============\n")
            awal.append(p)
            akhir.remove(p) # pindahkan dari list akhir ke awal

            if isValid(awal): # Cek jika list awal valid
                steps.append((f"{(p)} Kembali\n"))
                count += 1 # steps count

                hasil = solve(awal, akhir, "left", steps, count) # rekursi ke perahu kiri
                if hasil is not None: # Jika hasilnya bukan None (Tidak ada solusi), keluar
                    return hasil
            else: # Jika tidak valid ulangi semua perubahan dan coba lagi
                akhir.append(p)
                awal.remove(p)
                steps.pop()
                steps.pop()
                steps.pop()
    return None

awal = ["P1", "L1", "P2", "L2", "P3", "L3"]
akhir = []
steps = [] # Langkah-langkah
count = 1 # langkah ke-{count}

solution = solve(awal, akhir, "left", steps, count)
print("===============[X]===============\n")
print("Langkah-langkah menyeberang: ")
if solution:
    for step in solution:
        print(step)
else:
    print("Tidak ada solusi ditemukan.")
    quit()

print("===============[HASIL AKHIR]===============\n")
print(f"Sisi awal: {awal}")
print(f"Sisi akhir: {akhir}\n")
print("=================================")

''' Output program
===============[X]===============

Langkah-langkah menyeberang:
Sisi awal: ['P1', 'L1', 'P2', 'L2', 'P3', 'L3']
Sisi Akhir: []

===============[1]===============

('P1', 'L1') Menyebrang

Sisi awal: ['P2', 'L2', 'P3', 'L3']
Sisi Akhir: ['P1', 'L1']

===============[2]===============

P1 Kembali

Sisi awal: ['P2', 'L2', 'P3', 'L3', 'P1']
Sisi Akhir: ['L1']

===============[3]===============

('P2', 'L2') Menyebrang

Sisi awal: ['P3', 'L3', 'P1']
Sisi Akhir: ['L1', 'P2', 'L2']

===============[4]===============

L1 Kembali

Sisi awal: ['P3', 'L3', 'P1', 'L1']
Sisi Akhir: ['P2', 'L2']

===============[5]===============

('P3', 'L3') Menyebrang

Sisi awal: ['P1', 'L1']
Sisi Akhir: ['P2', 'L2', 'P3', 'L3']

===============[6]===============

P2 Kembali

Sisi awal: ['P1', 'L1', 'P2']
Sisi Akhir: ['L2', 'P3', 'L3']

===============[7]===============

('P1', 'L1') Menyebrang

Sisi awal: ['P2']
Sisi Akhir: ['L2', 'P3', 'L3', 'P1', 'L1']

===============[8]===============

L2 Kembali

Sisi awal: ['P2', 'L2']
Sisi Akhir: ['P3', 'L3', 'P1', 'L1']

===============[9]===============

('P2', 'L2') Menyebrang

===============[HASIL AKHIR]===============

Sisi awal: []
Sisi akhir: ['P3', 'L3', 'P1', 'L1', 'P2', 'L2']

=================================
'''