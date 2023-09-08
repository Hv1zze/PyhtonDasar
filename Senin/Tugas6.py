print("Input Nilai Siswa")
nilai = int(input("Masukan Nilai Siswa: "))
if nilai >= 75:
    print("Anda Tuntas")
else:
    print("Tidak Tuntas")

pilih = int(input("1. Mau \n2. Tidak \nApakah Anda Ingin Mengulang: "))
if pilih == 1:
    nilai = int(input("Masukan Nilai : "))
    if nilai >= 75:
        print("Tuntas")
    else: 
        print("Tidak Tuntas")
if pilih == 2:
    if nilai >= 75:
        print("Tuntas")
    elif nilai <= 75:
        print("Tidak Tuntas")
    else:
        print("TIdak Tuntas")