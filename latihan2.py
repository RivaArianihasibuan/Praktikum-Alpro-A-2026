try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

except Exception as error:
    print("Terjadi kesalahan:", error)

finally:
    print("Program selesai.")

