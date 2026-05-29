print("=" * 40)
print("PROGRAM LOOPING CATUR & AKTIVITAS")
print("=" * 40)

# =========================
# PAPAN CATUR
# =========================

print("\nLAYOUT PAPAN CATUR:\n")

for baris in range(8):
    for kolom in range(8):

        if (baris + kolom) % 2 == 0:
            print("⬜", end=" ")

        else:
            print("⬛", end=" ")

    print()

# =========================
# INPUT AKTIVITAS
# =========================

aktivitas_list = []

jumlah = int(input("\nBerapa aktivitas yang ingin dimasukkan? "))

for i in range(jumlah):

    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Masukkan nama aktivitas: ")
    waktu = input("Masukkan waktu aktivitas: ")
    prioritas = input("Masukkan prioritas (tinggi/sedang/rendah): ")

    data = {
        "aktivitas": aktivitas,
        "waktu": waktu,
        "prioritas": prioritas
    }

    aktivitas_list.append(data)

# =========================
# HASIL DATA
# =========================

print("\n" + "=" * 40)
print("DAFTAR AKTIVITAS USER")
print("=" * 40)

for index, item in enumerate(aktivitas_list, start=1):

    print(f"""
Aktivitas #{index}
Nama       : {item['aktivitas']}
Waktu      : {item['waktu']}
Prioritas  : {item['prioritas']}
""")

print("Semua aktivitas berhasil ditampilkan.")
