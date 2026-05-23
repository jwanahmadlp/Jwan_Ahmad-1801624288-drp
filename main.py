from datetime import datetime

print("=" * 40)
print("SISTEM MANAJEMEN AKTIVITAS")
print("=" * 40)

nama = input("Masukkan nama user: ")

while True:
    print("\nPilih aktivitas:")
    print("1. Sarapan")
    print("2. Berangkat Kerja")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        print("\nMenu Sarapan:")
        print("1. Telur")
        print("2. Mi Instan")
        print("3. Nugget")
        print("4. Roti")

        menu = input("Pilih menu: ")

        if menu == "1":
            print("\nKamu memilih Telur.")
            print("Telur perlu dimasak terlebih dahulu.")
            print("Estimasi memasak: 5 menit.")

        elif menu == "2":
            print("\nKamu memilih Mi Instan.")
            print("Mi Instan perlu dimasak terlebih dahulu.")
            print("Estimasi memasak: 10 menit.")

        elif menu == "3":
            print("\nKamu memilih Nugget.")
            print("Nugget perlu dimasak terlebih dahulu.")
            print("Estimasi memasak: 8 menit.")

        elif menu == "4":
            print("\nKamu memilih Roti.")
            print("Kamu harus membeli bahan atau roti terlebih dahulu.")

        else:
            print("\nMenu tidak tersedia.")

    elif pilihan == "2":
        sekarang = datetime.now()

        jam_masuk = 8
        menit_masuk = 0

        print("\nWaktu saat ini:",
              sekarang.strftime("%H:%M:%S"))

        if sekarang.hour > jam_masuk:
            print("PERINGATAN: Kamu terlambat masuk kerja!")

        elif sekarang.hour == jam_masuk and sekarang.minute > menit_masuk:
            print("PERINGATAN: Kamu terlambat masuk kerja!")

        else:
            print("Kamu masih tepat waktu untuk masuk kerja.")

    elif pilihan == "3":
        print(f"\nTerima kasih, {nama}.")
        print("Program selesai.")
        break

    else:
        print("\nInput tidak valid.")
        