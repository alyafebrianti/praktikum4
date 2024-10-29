## kode program 
```
 tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
if tipe_tiket == "reguler":
    harga_tiket = 35000
elif tipe_tiket == "vip":
    harga_tiket = 90000
else:
    print("Tipe tiket tidak valid.")
    harga_tiket = 0
if status_member == "ya" and harga_tiket > 0:
    diskon = harga_tiket * 0.3
    total_harga = harga_tiket - diskon
else:
    total_harga = harga_tiket
if harga_tiket > 0:
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
```

## output program
```
PS C:\Users\ASUS\Desktop\praktikum 1> & C:/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/ASUS/Desktop/praktikum 1/bioskop.py"
Masukkan tipe tiket (reguler/VIP): reguler
Apakah Anda memiliki kartu member? (ya/tidak): tidak
Total harga yang harus dibayar: Rp35000.00
PS C:\Users\ASUS\Desktop\praktikum 1> & C:/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/ASUS/Desktop/praktikum 1/bioskop.py"
Masukkan tipe tiket (reguler/VIP): reguler
Apakah Anda memiliki kartu member? (ya/tidak): ya
Total harga yang harus dibayar: Rp24500.00
PS C:\Users\ASUS\Desktop\praktikum 1>
```
## Cara Kerja Program
Program ini menghitung harga tiket dengan mempertimbangkan jenis tiket yang dibeli (reguler atau VIP) dan apakah pembeli memiliki kartu member yang memberikan diskon. Mari kita bahas setiap bagian:

1. **Input Jenis Tiket**:
   ```python
   tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
   ```
   Program meminta pengguna untuk memasukkan jenis tiket yang diinginkan, yaitu "reguler" atau "VIP". Input tersebut diubah menjadi huruf kecil dan dihilangkan spasi di depan dan belakang untuk memastikan konsistensi, sehingga "VIP" atau "vip" tetap dianggap sama.

2. **Input Status Member**:
   ```python
   status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
   ```
   Program meminta pengguna untuk memasukkan status apakah mereka memiliki kartu member ("ya" atau "tidak"). Penggunaannya mirip dengan input sebelumnya: diubah menjadi huruf kecil dan dihilangkan spasi.

3. **Menentukan Harga Tiket**:
   ```python
   if tipe_tiket == "reguler":
       harga_tiket = 35000
   elif tipe_tiket == "vip":
       harga_tiket = 90000
   else:
       print("Tipe tiket tidak valid.")
       harga_tiket = 0
   ```
   - Jika pengguna memilih tiket **reguler**, maka `harga_tiket` diatur menjadi **35.000**.
   - Jika pengguna memilih tiket **VIP**, maka `harga_tiket` diatur menjadi **90.000**.
   - Jika input tipe tiket tidak sesuai (bukan "reguler" atau "VIP"), program akan menampilkan pesan **"Tipe tiket tidak valid."** dan `harga_tiket` diatur menjadi **0**.

4. **Menghitung Diskon untuk Member**:
   ```python
   if status_member == "ya" and harga_tiket > 0:
       diskon = harga_tiket * 0.3
       total_harga = harga_tiket - diskon
   else:
       total_harga = harga_tiket
   ```
   - Jika pengguna adalah **member** (jawaban "ya") dan memilih tipe tiket yang valid (`harga_tiket > 0`), maka mereka mendapatkan diskon sebesar **30%** dari `harga_tiket`.
   - Jika pengguna **bukan member** atau tipe tiket tidak valid, maka `total_harga` sama dengan `harga_tiket` tanpa diskon.

5. **Menampilkan Total Harga**:
   ```python
   if harga_tiket > 0:
       print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
   ```
   - Jika harga tiket valid (`harga_tiket > 0`), program akan mencetak total harga yang harus dibayar, diformat hingga dua desimal (contoh: Rp35000.00).
   
Dengan struktur ini, program memastikan harga tiket dihitung dengan benar sesuai tipe tiket dan status keanggotaan pengguna.

## kode program 
```
# Fungsi untuk menghitung berdasarkan operator
def kalkulator(angka1, angka2, operator):
    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Kesalahan: Pembagian dengan nol tidak diperbolehkan"
    else:
        return "Operator tidak valid"

# Meminta input dari pengguna
try:
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    # Menghitung hasil berdasarkan input
    hasil = kalkulator(angka1, angka2, operator)

    # Menampilkan hasil
    print(f"Hasil: {hasil}")

except ValueError:
    print("Input tidak valid! Pastikan Anda memasukkan angka.")
 ```

## output program
```
PS C:\Users\ASUS\Desktop\praktikum 1> & C:/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/ASUS/Desktop/praktikum 1/iga.py"
Masukkan angka pertama: 122
Masukkan operator (+, -, *, /): +
Masukkan angka kedua: 12
Hasil: 134.0
PS C:\Users\ASUS\Desktop\praktikum 1> & C:/Users/ASUS/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/ASUS/Desktop/praktikum 1/iga.py"
Masukkan angka pertama: 130 
Masukkan operator (+, -, *, /): *
Masukkan angka kedua: 2
Hasil: 260.0
PS C:\Users\ASUS\Desktop\praktikum 1>
```
