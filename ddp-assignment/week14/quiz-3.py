class kasir :
    def __init__(self, nama, uang) :
        self.nama = nama
        self.uang = uang
        
    def makanan(self, pilihan):
        foods ={
            "biskuit" : 5000,
            "waffer" : 3000,
            "coklat" : 15000,
            "popmie" : 4000,
            "chiki" : 5000
        }
        
        harga = foods[pilihan]
        self.uang -= harga
        print("Terimakasih atas pembelian anda")
        print("daftar pembelian anda", pilihan)
        print("//--------------------------------//")
        print("TOTAL = ", harga)
        print("sisa uang anda = ", self.uang)
        
    def minuman(self, pilihan):
        drinks = {
            "jus" : 7000,
            "susu" : 6000,
            "jamu" : 5000,
            "pocari" : 8000,
            "teh" : 4000
        }
        
        harga = drinks[pilihan]
        self.uang -= harga
        print("Terimakasih atas pembelian anda")
        print("daftar pembelian anda", pilihan)
        print("//--------------------------------//")
        print("TOTAL = ", harga)
        print("sisa uang anda = ", self.uang)
        
        
print()
toko = kasir(input("Nama anda = "), int(input("Masukkan nominal uang anda untuk transaksi = ")))
print()
toko.makanan(input("Masukkan makanan pilihan anda = "))
print()
toko.minuman(input("Masukkan minuman pilihan anda = "))
