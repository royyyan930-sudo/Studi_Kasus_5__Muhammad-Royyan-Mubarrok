# Membuat Function dan parameter untuk menghitung biaya menginap di hotel
def menghitung_biaya(jenis_kamar, durasi_menginap):
    if jenis_kamar == "standar":
        biaya_per_malam = 200000
    elif jenis_kamar == "deluxe":
        biaya_per_malam = 350000

# menghitung total biaya menginap
    total_biaya = biaya_per_malam * durasi_menginap
    return total_biaya

# Program utama
print("Selamat datang di Hotel Kami!")

# Meminta input dari pemgguna
jenis_kamar = input("Masukkan jenis kamar (standar/deluxe): ")

check_in = int(input("masukkan tanggal check-in (1-31): "))
check_out = int(input("masukkan tanggal check-out (1-31): "))

# menghitung lama menginap
lama_menginap = check_out - check_in

# menghitung total biaya menginap
total_biaya = menghitung_biaya(jenis_kamar, lama_menginap)

# menampilkan hasil perhitungan
print("Jenis kamar yang dipilih:", jenis_kamar)
print("Tanggal check-in:", check_in)
print("Tanggal check-out:", check_out)
print("Durasi menginap:", lama_menginap, "malam")
print("Total biaya menginap adalah:", total_biaya)