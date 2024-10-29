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
