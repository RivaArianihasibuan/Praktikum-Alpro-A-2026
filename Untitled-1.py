class Buah:
    def __init__(self, bentuk, rasa, warna):
        self.bentuk = bentuk
        self.rasa = rasa
        self.warna = warna

    def info_buah(self):
        print("Bentuk :", self.bentuk)
        print("Rasa   :", self.rasa)
        print("Warna  :", self.warna)

    def ubah_rasa(self, rasa_baru):
        self.rasa = rasa_baru
        print("Rasa buah diubah menjadi:", self.rasa)

    def alamat(self):
        print("pekanbaru")    


p1 = Buah("bulat", "asam", "orange")
p2 = Buah("panjang", "manis", "kuning")
p3 = Buah("oval", "kecut", "hijau")

p1.info_buah()
p2.ubah_rasa("pahit")
p3.alamat()

