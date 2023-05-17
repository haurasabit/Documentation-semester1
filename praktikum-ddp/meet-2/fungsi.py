def greeting(hour) :
    if hour < 12 :
        return 'Selamat Pagi'
    elif hour > 18 : 
        return 'Selamat Sore'
    else:
        return 'Selamat Malam'

print(greeting(7))
print()


#pake = 1 dlm parameter sebagai default bawaan dr python ny sendiri
#misal mo print kita tdk perlu masukin angka pada parameter yg dibawah
def greeting(hour = 1) :
    if hour < 12 :
        return 'Selamat Pagi'
    elif hour > 18 : 
        return 'Selamat Sore'
    else:
        return 'Selamat Malam'

print(greeting())