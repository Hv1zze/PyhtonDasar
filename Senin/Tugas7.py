print("Gaji Pokok")
nama=input("Masukkan nama Anda : ")
gajiPokok=int(input("Masukkan gaji pokok Anda : "))
tunjangan=20/100*gajiPokok
pajak=15/100*(gajiPokok+tunjangan)
gajiBersih=gajiPokok+tunjangan-pajak

print("\n\t\tDetail Gaji Pekerja\n")
print(f"Nama : {nama}")
print(f"Gaji Pokok : {gajiPokok}")
print(f"Tunjangan : {tunjangan}")
print(f"Pajak : {pajak}")
print(f"Gaji Bersih : {gajiBersih}")