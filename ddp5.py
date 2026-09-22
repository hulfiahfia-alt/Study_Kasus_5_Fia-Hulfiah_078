
def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    else:
        tarif = 0
        print("jenis kendaraan tidak dikenali!")

    total_biaya = tarif * lama_parkir
    return total_biaya

jenis_kendaraan = input("masukkan jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("masukkan jam masuk: "))
jam_keluar = int(input("masukkan jam keluar: "))

lama_parkir = jam_keluar - jam_masuk
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("\n===== struk parkir =====")
print("jenis kendaraan :", jenis_kendaraan)
print("jam masuk       :", jam_masuk,":00")
print("jam keluar      :", jam_keluar,":00")
print("lama parkir     :", lama_parkir,"jam")
print("total biaya     : Rp", total_biaya)