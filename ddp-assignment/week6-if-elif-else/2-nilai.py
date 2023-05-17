nama = input("Nama : ")
kelas = input("Kelas : ")
nilai = int( input("Nilai kamu? = ") )

print ("Halo,", nama, "kelas", kelas, "Selamat Datang!")
print("dengan nilai", nilai, "kamu dinyatakan")

if nilai >= 90 :
    print("ISTIMEWA")
    
elif nilai >=70 :
    print("SANGAT BAGUS")
    
elif nilai >=60 :
    print("CUKUP")
    
else :
    print("GAGAL!")