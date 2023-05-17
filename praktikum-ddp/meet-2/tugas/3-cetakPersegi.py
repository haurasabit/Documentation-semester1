# kita buat inputan, kira2 mau berapa panjang dan lebar persegi yang kita inginkan
n = int(input("masukkan mau buat panjang berapa = "))
m = int(input("masukkan mau buat lebar berapa = "))


# lalu gunakan perulangan untuk membuat persegi dari #
# for i in untuk membuat perulangan panjang kebawah
# for j in untuk membuat perulangan lebar kesamping
# lalu kita print dengan didefinisikan dengan tanda #
# dan gunakan end =" " untuk membuat spasi antar #
for i in range(n):
    for j in range(m):
        print("#", end=" ")
        
    print()
    #lalu cetak deh
