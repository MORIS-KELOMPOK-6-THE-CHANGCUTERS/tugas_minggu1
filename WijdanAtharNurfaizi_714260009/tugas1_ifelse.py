# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama     : Wijdan Athar Nurfaizi
# NIM      : 714260009
# kelompo  : THE CHANGCUTERS
# Kelas    : 11 A
# ==================================================

print("=" *40)
nilai = float(input("Masukkan nilai akhir (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid! Masukkan nilai antara 0 sampai 100.")
else:
    if nilai >= 80:
        huruf = "A"
        keterangan = "LULUS"
    elif nilai >= 70:
        huruf = "B"
        keterangan = "LULUS"
    elif nilai >= 60:
        huruf = "C"
        keterangan = "LULUS"
    elif nilai >= 50:
        huruf = "D"
        keterangan = "TIDAK LULUS"
    elif nilai <= 45:
        huruf = "E"
        keterangan = "TIDAK LULUS"

    print(f"Nilai: {nilai}")
    print(f"Huruf mutu: {huruf}")
    print(f"Keterangan: {keterangan}")