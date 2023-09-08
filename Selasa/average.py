def hitung_rata_rata(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return rata_rata


def input_angka():
    angka = []
    while True:
        try:
            bilangan = float(input("Masukkan Angka (0 Untuk Mengakhiri): "))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("Masukkan Angka Yang Valid.")
    return angka


if __name__ == "__main__":
    print("Program Menghitung Rata-rata ")
    daftar_angka = input_angka()

    if daftar_angka:
        rata_rata = hitung_rata_rata(daftar_angka)
        print(f"Rata-rata Angka-Angka Yang Dimasukkan Adalah: {rata_rata:.2f}")
    else:
        print("Tidak Ada Angka Yang Dimasukkan.")