# Study_Kasus_5_Fia-Hulfiah_078
Nama: Fia Hulfiah
NIM: 2609116078
Kelas: B

PENJELASAN KODE PROGRAM
1. Function hitung_biaya_parkir(jenis_kendaraan, lama_parkir)
   
   function berfungsi untuk menghitung total biaya parkir. Menerima dua parameter yaitu, jenis_kendaraan (untuk menetukan       tarif), lama_parkir (untuk menentukan berapa lama kendaraan parkir).

2. Percabangan if/elif/else
   
   digunakan untuk menentukan tarif sesuai jenis kendaraan:

   jika "mobil": tarif Rp5.000/jam
   
   jika "motor": tarif Rp3.000/jam
   
   jika bukan keduanya: tarif Rp0 dan akan muncul pesan "jenis kendaraan tidak dikenali"

3. Menghitung Total Biaya
   
   total_biaya = tarif * lama parkir

   (tarif per jam dikalikan lama kendaraan parkir)

4. Return Value
   
   return total_biaya, mengembalikan hasil perhitungan ke bagian program yang memanggil function, sehingga nilainya biasa       disimpulkan ke variabel dan digunakan kembali.

5. Input Data
    
   Program meminta input jenis kendaraan, jam masuk, jam keluar dari user menggunakan input()

6. Menghitung Lama Parkir
    
   lama_parkir = jam_keluar - jam_masuk
   (lama parkir didapat dari selisih jam keluar dan jam masuk)

7. Memanggil Function
    
   total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

   function dipanggil dengan mengirim jenis kendaraan dan lam parkir sebagai argument, hasilnya disimpan ke variabel            total_biaya.

8. Menampilkan Hasil
    
   program menampilkan struk parkir berisi jenis kendaraan, jam masuk, jam keluar, lam parkir, dan total biaya menggunakan      print().

<img width="1924" height="1084" alt="Screenshot 2026-09-22 233706" src="https://github.com/user-attachments/assets/996fd984-09d2-4031-9d62-3863902eaeda" />



