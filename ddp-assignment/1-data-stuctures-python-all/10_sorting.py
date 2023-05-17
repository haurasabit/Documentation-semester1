#returns a new list of items in sorted order
#doesn't change the original list
#g mengubah daftar asli fungsi yg diurutkan, urutannya pun g diubah

#sting
x = "bug"
print(sorted(x))

#list
y = ["pig", "cow", "horse"]
print(sorted(y))

#tuple
z = ("kevin", "niklas", "johnny", "clark")
print(sorted(z))

#SORTING : sort by second letter
#add a key parameter and a lambda function to return the second character
#the word key is a defined parameter name, k is an arbirary variable name

z = ("kevin", "niklas", "johnny", "clark")
print(sorted(z, key = lambda k : k[1]))

#dengan lambda km bisa mengurutkan barang dengan urutan terbalik
#atau menggunakan beberapa parameter lain 
#gunakan kunci yg sama dengan beberapa fungsi lambda
#jd untuk setiap item K dpt melakukannya lagi
#kita akan mengambil satu item yg merupakan huruf kedua, so nanti akan menjadi 
#e i l o
# e for kEvin, i for nIklas, l for cLark, o for jOhnny
# 1 berarti kita menempatkannya dlm urutan yg diurutkan berdasarkan huruf kedua
# dan kita dpt melihat bahwa huruf kedua tsb berurutan berdasarkan abjad 