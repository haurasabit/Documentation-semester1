banyakNumber = int(input("Masukkan banyak angka yang mau di rata-rata : "))
# gunakan variabel untuk input banyaknya angka yang ingin kita rata-rata kan
# gunakan int() agar bisa didefinisikan bahwa itu integer/ sebuah numerik

listNumber = []
#data tipe list, berfungsi utk menambahkan objek di dlmnya
# [] kosong karena kita akan mengisi data nya tsb dgn yg dibawah ini

addNumber = 0
# variabel number kita isi dengan angka nol di awal


#kita taro variabel number dalam fungsi for ini utk melakukan perulangan
#dan gunakan fungsi range untuk membuat batasannya
for number in range (banyakNumber):
    inputNumber = int(input("Masukkan angka ke-%d : " % (number + 1)))
    # disitu kita akan input dan cetak angka dgn tipe integer
    # kita gunakan fungsi input utk memasukkan berapa angka yg kita ingin hitung rata-ratanya
    # %d sebagai pengganti angka ke-n yg blm didefinisikan
    # % (number + 1) untuk mendefinisikan nilai nya, krn kita memulai dari angka 1
    
    listNumber.append(inputNumber)
    # append ini untuk menambahkan nilai dibagian akhir suatu list
    # 
    
    addNumber += listNumber[number]
    #kita jumlahkan addnumber dgn number yg ada di listNumber
    
    average = addNumber / banyakNumber
    # kita hitung rata-ratanya
    
print("Rata-rata = %0.2f" % average)
# cetak hasil dari perulangan
# %0.2f adalah angka yang dibelakang koma ada 2
# % average mengimplementasikan %0.2f.
# jadi a50.2f adalah dua angka dibelakang koma dr variable average