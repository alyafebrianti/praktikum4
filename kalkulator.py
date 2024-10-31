def kalkulator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        print("Input tidak valid")
        exit()

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator '+', '-', '*', atau '/': ")

hasil = kalkulator(a, b, operator)
print(f"Hasilnya adalah {hasil}")