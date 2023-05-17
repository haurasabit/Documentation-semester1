# menggunkan perulangan for utk mencetak bilangan genap 100 - 2

#beri variabel awal dulu
task = "cetak perulangan FOR bilangan genap dari 100 - 2" 
#lalu cetak variable tersebut untuk penjelasan saat di run

# gunakan for untuk perulangan,
#lalu gunakan fungsi reversed untuk membalikan urutan dari yg terbesar ke terkecil
for a in reversed(range(2, 101, 2)):
    print(a)
    #dimaksud range(2, 101, 2) disini adalah kita memulai dari angka 2 dan berakhir di 100
    #dan karena yg diminta angka genap, jd kita bisa masukkan 2 di terakhir sebagai selang 1.
    #lalu yg dimaksud reversed() adalah untuk membalikkan, yg tadinya dari angka 2 - 100, menjadi 100 - 2