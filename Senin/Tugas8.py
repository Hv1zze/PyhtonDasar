print("Program Hitung Umur")
nilai = int(input("Masukkan Umur Anda: "))
if nilai <= 10:
    print("Anak-Anak")
elif 10 < nilai < 18:
    print("Remaja")
elif 18 < nilai < 35:
    print("Dewasa")
elif 35 < nilai < 65:
    print("Parubaya")
else:
    print("Tua")