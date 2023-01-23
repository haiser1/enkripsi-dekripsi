import modul
import os


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("="*30)
    print("Pilih Menu:")
    print("0. Keluar")
    print("1. Enkripsi")
    print("2. Deskripsi")
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
            modul.enkripsi("folder_key", "folder_path")
        elif pilihan == "2":
            modul.enkripsi_file("folder_key", "file_path")
        else:
            print("Inputan Tidak Valid...!!!!")

    elif menu == "2":
        print("="*30)
        print("1. Deskripsi Folder")
        print("2. Deskripsi File")
        print("="*30)
        pilih = input("Input Deskripsi Yang Anda Inginkan(1/2): ")
        if pilih == "1":
            modul.deskripsi("folder_key", "folder_path")
        elif pilih == "2":
            modul.deskripsi_file("key", "file_path")
        else:
            print("Inputan Tidak Valid...!!!!")

    else:
        print("Inputan Tidak Valdi!!!!")
    keluar = input("Apakah Anda Ingin Keluar Dari Program(y/n)?? ")
    if keluar == "y":
        print("Anda Keluar Dari Program, bye bye....")
        break 
    elif keluar == "n":
        print("lanjut")
    else:
        print("Inputan Tidak Valid")


