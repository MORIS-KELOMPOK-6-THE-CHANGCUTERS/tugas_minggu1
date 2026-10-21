# =====================================
# Tugas Sesi Kelas (Latihan Individu)
# Nama : Rahmatan Gani
# NIM  : 714260001
# kelompok : 6 THE CHANGCUTERS
# kelas : 1A


print("=" * 50)
print("     Program Kalkulator Sederhana")
print("=" * 50)

try:
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    operator = input("Pilih operasi (+, -, *, /): ").strip()

    print("=" * 50)
    if operator == "+":
        print(f"Hasil penjumlahan {a} + {b} = {a + b}")
    elif operator == "-":
        print(f"Hasil pengurangan {a} - {b} = {a - b}")
    elif operator == "*":
        print(f"Hasil perkalian {a} * {b} = {a * b}")
    elif operator == "/":
        if b != 0:
            print(f"Hasil pembagian {a} / {b} = {a / b}")
        else:
            print("Maaf, pembagian dengan nol tidak bisa dilakukan.")
    else:
        print(f"Peringatan: operator '{operator}' tidak dikenali.")
        print("Gunakan salah satu: +, -, *, /")

except ValueError:
    print("Input tidak valid. Masukkan angka, bukan huruf.")

print("=" * 50)
print("Terima kasih sudah menggunakan kalkulator ini!")
print("=" * 50)