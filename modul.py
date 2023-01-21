from cryptography.fernet import Fernet
import os

def enkripsi(folder_key, folder_path):
# input untuk file tempat key
    folder_key = input("Buat Nama File Untuk Menyimpan Key, Misal(key.key) : ")
    key = Fernet.generate_key()
    with open(folder_key, 'wb') as key_file:
        key_file.write(key)
        cipher = Fernet(key)
        print("Key Berhasil Dibuat.....")
            
    
    folder_path = input("Input Path Folder Yang Ingin Dienkripsi, misal(D:\path\Folder) :")
    if os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        data = f.read()
                        # enkripsi
                        encrypted_data = cipher.encrypt(data)
                    with open(file_path, 'wb') as f:
                        f.write(encrypted_data)
                        print("Semau File di Dalam Folder Berhasil Di Enkripsi....")
    else:
        print("Path Folder Tidak Valid.....!!!")
            

def deskripsi(key, folder_path):
    key = input("Input Key Yang Sudah Anda Buat Saat Melakukan Enkripsi(buka file key anda lalu copas disini) : ")
    try:
        cipher = Fernet(key)
    except:
        print("Key Tidak Valid...!!!!")
        return

    try:    
        folder_path = input("Input Folder Yang Ingin Dideskripsi, misal(D:\path\Folder) :")
        if os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        data = f.read()
                        decrypted_data = cipher.decrypt(data)
                    with open(file_path, 'wb') as f:
                        f.write(decrypted_data)
                        print("Deskripsi Berhasil.....")
        else:
            print("Path Folder Anda Tidak Valid..!!!")
    except:
        print("Deskripsi File Gagal....!!!")
        print("Key Yang Anda Masukan Salah....!!!")
    
        

def enkripsi_file(folder_key, file_path):
    folder_key = input("Buat Nama File Untuk Menyimpan Key, Misal(key.key) : ")
    key = Fernet.generate_key()
    with open(folder_key, 'wb') as key_file:
        key_file.write(key)
        cipher = Fernet(key)
        print("Key Berhasil Dibuat....")

    file_path = input("Input Path File Yang Ingin Di Enkripsi, Misal(D:\path\File.txt) :")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            data = file.read()
            cipher_text = cipher.encrypt(data)

        with open(file_path, "wb") as file:
            file.write(cipher_text)
            print("File Berhasil di Enkripsi.....")
            
    else:
        print("Path File Tidak Valid....!!!")

def deskripsi_file(key, file_path):
    key = input("Input Key Yang Sudah Anda Buat Saat Melakukan Enkripsi : ")
    try:   
        cipher = Fernet(key)
    except:
        print("Key Tidak Valid....!!")
        return
    try:
        file_path = input("Input File Yang Ingin di deskripsi, Misal(D:\path\file.txt): ")
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                data = file.read()
                deskrip_data = cipher.decrypt(data)
            with open(file_path, 'wb') as file:
                file.write(deskrip_data)
                print("File Anda Berhasil di Deskripsi.....")
        else:
            print("Path File Invalid....!!!!")

    except:
        print("Deskripsi File Gagal....!!!")
        print("Key Yang Anda Masukan Salah....!!!")
                

