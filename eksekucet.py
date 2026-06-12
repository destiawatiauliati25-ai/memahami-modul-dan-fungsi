import aritmatika
import konversi
import ubah_bilangan

while True:
    print ("Menu Utama: ")
    print("1. Aritmatika")
    print("2. Konversi")
    print("3. Ubah Bilangan: ")
    print("4. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        print("Aritmatika")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")

        p = input("Pilih Menu: ")

        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))

        if p == "1":
            print("Hasil = ", tambah(a,b))
        elif p == "2":
            print("Hasil = ", pangkat(a,b))
        elif p == "3":
            print("Hasil = ", kali(a,b))
        else:
            print("Pilihan salah, ulangi!!")

    elif pilihan == "2":
        print("Konversi")
        print("1. cm ke m")
        print("2. m ke cm")

        p = input("Pilih konversi: ")

        nilai = float(input("Masukkan nilai: "))

        if p == "1":
            print("Hasil = ", cm_m(nilai), "m")
        elif p == "2":
            print("Hasil = ", m_cm(nilai), "cm")
        else:
            print("Pilihan salah, ulangi!!")

    elif pilihan == "3":
        print("Ubah Bilangan")
        print("1. Desimal ke Biner")
        print("2. Desimal ke Oktal")
        print("3. Desimal ke Hexadesimal")

        p = input("Pilih Konversi: ")

        nilai = int(input("Masukkan bilangan Desimal: "))

        if p == "1":
            print("Hasil = ", desimal_biner(nilai))
        elif p == "2":
            print("Hasil = ", desimal_oktal(nilai))
        elif p == "3":
            print("Hasil = ", desimal_hexadesimal(nilai))
        else:
            print("Pilihan salah, ulangi!!")

    elif pilihan == "4":
        print("Terima Kasih")
        break

    else:
        print("Pilihan salah, ulangi!!")