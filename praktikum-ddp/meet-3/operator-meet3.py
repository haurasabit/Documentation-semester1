number1 = 5
number2 = 10

#operator perbandingan
print(number1 != number2)

if number1 != number2:
    print("nomor berbeda")
else:
    print("nomor sama!")
    

#OPERATOR LOGIKA
if number1 > 99 and number1 < 1000:
    print("ini bilangan ratusan!")
else :
    print("Bukan bilangan ratusan")
    

#OPERATOR ARITMATIKA
while True:
    number3 = int(input("Masukkan angka : "))
    
    if number3 == 00:
        break
    if number3 %2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")