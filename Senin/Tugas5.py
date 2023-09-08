print("=======================================")
print('##  Program Python Piramida Bintang  ##')
print('=======================================')
print()
tPiramid = int(input('Input tinggi piramida: '))
print()

for i in range(tPiramid):
  for j in range(i+1):
    print(' *',end='')
  print()