data_angka = [10, 20, 30]

try:
    posisi = int(input("Masukkan index (0-2): "))
    hasil = data_angka[posisi]
    print(f"Nilai pada index {posisi} adalah {hasil}")

except ValueError:
    print("Terjadi kesalahan: input harus berupa angka bulat!")

except IndexError:
    print("Terjadi kesalahan: index berada di luar jangkauan list!")

finally:
    print("Program selesai dijalankan.")
