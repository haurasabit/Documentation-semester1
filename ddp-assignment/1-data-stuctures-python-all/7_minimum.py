#pemeriksaan python secara leksikografis yang
#berarti yang terkecil pada skala ASCII
#sehingga kamu dpt menggunakan fungsi minimum pada alfa/numerik
#tapi kamu g bisa mencampur tipe alpa dan numerik ke dlm daftar, ntar eror

#sting
x = "bug"
print(min(x))

#list
y = ["pig", "cow", "horse"]
print(min(y))

#tuple
z = ("kevin", "mark", "johnny", "jade")
print(min(z))

#string akan mencetak B , dlm daftar minimun, urutan abjad b paling awal kan..
#list akan tercetak cow , krn huruf c adalah yg paling kecil, dilihat dr urutan abjad
#tuple mencetak yg pertama menurut abjad juga yaitu jade --> huruf j ada dua, namun jade menjadi yg minimum krn stelah j adalah a

