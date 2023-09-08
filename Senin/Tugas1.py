print('##  Program Menghitung dan Mencetak Keliling dan Luas Persegi, Persegi Panjang dan Trapesium  ##')
print('================================================================================================')
print("1. Persegi \n2. Persegi Panjang \n3. Trapesium")
pil = int(input("Masukan Pilihan Anda: "))

if pil == 1:
    print("Persegi")
    keliling = int(input("Masukan Sisi (Keliling): "))
    luas = int(input("Masukan Sisi (Luas): "))
    kel = keliling * 4
    totalluas = luas * luas
    print("Keliling Persegi: ", kel)
    print("Luas Persegi: ", totalluas)
elif pil == 2:
    print("Persegi Panjang")
    panjang = int(input("Masukan Panjang: "))
    lebar = int(input("Masukan Lebar: "))
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    print("Keliling Persegi Panjang: ", keliling)
    print("Luas Persegi Panjang: ", luas)
elif pil == 3:
    print("Trapesium")
    alasa = int(input("Masukan Alas A: "))
    alasb = int(input("Masukan Alas B: "))
    sisi1 = int(input("Masukan Sisi 1: "))
    sisi2 = int(input("Masukan Sisi 2: "))
    tinggi = int(input("Masukan Tinggi Trapesium: "))
    luas = 0.5 * (alasa + alasb) * tinggi
    keliling = alasa + alasb + sisi1 + sisi2
    print(f"Luas Trapesium: {luas} \nKeliling Trapesium: {keliling} ")
else: 
    print("Tidak ada pilihan")