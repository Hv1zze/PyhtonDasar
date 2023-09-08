print("=========================================")
print("Program Menghitung Volume Balok dan Kubus")
print("=========================================")
print("1. Balok \n2. Kubus")
pil = int(input("Masukkan Pilihan Anda: "))

if pil == 1:
    print("Balok")
    panjang = int(input("Masukkan Panjang: "))
    lebar = int(input("Masukkan Lebar: "))
    tinggi = int(input("Masukkan Tinggi: "))
    volume = panjang * lebar * tinggi
    print("Volume Balok: ", volume)
elif pil == 2:
    print("Kubus")
    sisi = int(input("Masukkan Panjang Sisi: "))
    volume = sisi * sisi * sisi
    print("Volume Kubus: ", volume)
else:
    print("Pilihan tidak valid. Pilih 1 untuk Balok atau 2 untuk Kubus.")