# Custom Exception
class NamaError(Exception):
    def __init__(self, nama):
        super().__init__(f"Nama '{nama}' terlalu pendek! Minimal 3 karakter.")

class UsiaError(Exception):
    def __init__(self, usia):
        super().__init__(f"Usia '{usia}' tidak sesuai (17-60 tahun).")

class EmailError(Exception):
    def __init__(self, email):
        super().__init__(f"Email '{email}' tidak valid! Harus ada '@'.")

class NoHpError(Exception):
    def __init__(self, no_hp):
        super().__init__(f"No HP '{no_hp}' tidak valid! Harus 10-13 digit angka.")

# Fungsi Validasi
def cek_nama(nama):
    if len(nama) < 3:
        raise NamaError(nama)

def cek_usia(usia):
    if usia < 17 or usia > 60:
        raise UsiaError(usia)

def cek_email(email):
    if "@" not in email:
        raise EmailError(email)

def cek_no_hp(no_hp):
    if not no_hp.isdigit() or not (10 <= len(no_hp) <= 13):
        raise NoHpError(no_hp)

# Input data peserta
print("=== FORM REGISTRASI PESERTA ===")

# Nama
while True:
    try:
        nama = input("Masukkan Nama Lengkap: ")
        cek_nama(nama)
        break
    except NamaError as e:
        print("[ERROR]", e)

# Usia
while True:
    try:
        usia = int(input("Masukkan Usia: "))
        cek_usia(usia)
        break
    except ValueError:
        print("[ERROR] Usia harus angka!")
    except UsiaError as e:
        print("[ERROR]", e)

# Email
while True:
    try:
        email = input("Masukkan Email: ")
        cek_email(email)
        break
    except EmailError as e:
        print("[ERROR]", e)

# No HP
while True:
    try:
        no_hp = input("Masukkan No HP: ")
        cek_no_hp(no_hp)
        break
    except NoHpError as e:
        print("[ERROR]", e)

print("\n=== DATA TERDAFTAR ===")
print(f"Nama   : {nama}")
print(f"Usia   : {usia} tahun")
print(f"Email  : {email}")
print(f"No HP  : {no_hp}")
print("Status : TERDAFTAR")