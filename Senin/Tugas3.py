print("=============================================")
print("Menghitung dan Mencetak Pada Ganjil dan Genap")
print("=============================================")
angka1 = int(input("Masukan Angka 1: "))
angka2 = int(input("Masukan Angka 2: "))
cara = input("Pilih Operator (+, -, *, :): ")

if cara == "+":
    total = angka1 + angka2
    print(f"Total: {total}")
elif cara == "-":
    total = angka1 - angka2
    print(f"Total: {total}")
elif cara == "*":
    total = angka1 * angka2
    print(f"Total: {total}")
elif cara == "/":
    total = angka1 / angka2
    print(f"Total: {total}")
else:
    print("Wat the dog doin")

if total % 2 == 1:
    print("Hasil adalah Ganjil")
else:
    print("Hasil adalah Genap")