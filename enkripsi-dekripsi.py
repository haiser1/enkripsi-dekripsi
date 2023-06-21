import modul
import os

keluar = ""
while keluar != "y":
    os.system("cls" if os.name == "nt" else "clear")
    print("="*30)
    print("Pilih Menu:")
    print("0. Keluar")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("="*30)

    menu = input("Input Menu : ")
    if menu == "0":
        print("Anda Keluar Dari Program, bye bye....")
        break

    elif menu == "1":
        print("="*30)
        print("1. Enkripsi Folder (akan mengenkripsi semua file yang ada di dalam folder)")
        print("2. Enkripsi File (akan mengenkripsi File yang anda tentukan)")
        print("="*30)
        pilihan = input("Input Enkripsi Yang Anda Inginkan(1/2): ")
        if pilihan == "1":
            modul.enkripsi()
        elif pilihan == "2":
            modul.enkripsi_file()
        else:
            print("Inputan Tidak Valid...!!!!")

    elif menu == "2":
        print("="*30)
        print("1. Dekripsi Folder")
        print("2. Dekripsi File")
        print("="*30)
        pilih = input("Input Dekripsi Yang Anda Inginkan(1/2): ")
        if pilih == "1":
            modul.deskripsi()
        elif pilih == "2":
            modul.deskripsi_file()
        else:
            print("Inputan Tidak Valid...!!!!")

    else:
        print("Inputan Tidak Valdi!!!!")
    keluar = input("Apakah Anda Ingin Keluar Dari Program(y/n)?? ")
    


