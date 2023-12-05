# PythonPractice6

## Latihan 1

    import math

    Fungsi kuadrat jika hanya satu argumen
    a = lambda x: x**2 if isinstance(x, (int, float)) else None

    Fungsi pythagoras jika dua argumen numerik diberikan
    b = lambda x, y: math.sqrt(x**2 + y**2) if isinstance(x, (int, float)) and isinstance(y, (int, float)) else None

    Fungsi rata-rata jika minimal dua argumen numerik diberikan
    c = lambda *args: sum(args) / len(args) if all(isinstance(arg, (int, float)) for arg in args) and len(args) > 0 else None

    Fungsi menghapus duplikat karakter dari string
    d = lambda s: "".join(set(s)) if isinstance(s, str) else None

In this revised version, the original functions are replaced with lambda functions. Each lambda function is assigned to a variable (a, b, c, and d) that has the same name as the original function. 

The lambda function a takes a single argument, x, and returns x squared. 

The lambda function b takes two arguments, x and y, and returns the square root of the sum of x squared and y squared. 

The lambda function c takes any number of arguments, which are collected into a list called args. It returns the average of these arguments

The lambda function d takes a single argument, s, which is a string. It returns a new string that contains only the unique characters of s.

The unique characters are obtained by converting s to a set, which automatically removes duplicate characters.

## Tugas Praktikum

    # Inisialisasi daftar nilai mahasiswa
    daftar_nilai = []

A list named daftar_nilai is initialized to store information about students, including their names and grades.

    # Fungsi tambah untuk menambah data
    def tambah():
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa = {'Nama': nama, 'Nilai': nilai}
        daftar_nilai.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} dengan nilai {nilai} telah ditambahkan.")

This function prompts the user to input the student's name and grade.

Converts the grade input to a float.

Creates a dictionary (data_mahasiswa) with the student's name and grade.

Appends the dictionary to the daftar_nilai list.

Prints a confirmation message.

    # Fungsi tampilkan untuk menampilkan data
    def tampilkan():
        if not daftar_nilai:
            print("Daftar nilai mahasiswa kosong.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for data in daftar_nilai:
                print(f"Nama: {data['Nama']}, Nilai: {data['Nilai']}")

This function checks if the daftar_nilai list is empty. If it is, it prints a message indicating that the list is empty.

If the list is not empty, it iterates through the list and prints the names and grades of the students.

    # Fungsi hapus untuk menghapus data berdasarkan nama
    def hapus():
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        for data in daftar_nilai:
            if data['Nama'] == nama:
                daftar_nilai.remove(data)
                print(f"Data mahasiswa {nama} telah dihapus.")
                return
        print(f"Tidak ditemukan data mahasiswa dengan nama {nama}.")

This function prompts the user to input the name of the student whose data will be deleted.

It iterates through the daftar_nilai list, removes the entry with the specified name, and prints a confirmation message.

If no match is found, it prints a message indicating that no data was found for the specified name.

    # Fungsi ubah untuk mengubah data berdasarkan nama
    def ubah():
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        nilai_baru = float(input("Masukkan nilai baru: "))
        for data in daftar_nilai:
            if data['Nama'] == nama:
                data['Nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} telah diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Tidak ditemukan data mahasiswa dengan nama {nama}.")

This function prompts the user to input the name of the student whose data will be modified and the new grade.

It iterates through the daftar_nilai list, finds the entry with the specified name, updates the grade, and prints a confirmation message.

If no match is found, it prints a message indicating that no data was found for the specified name.

    while True:
        print("\n=== Menu Pilihan ===")
        print("1. Tambah Nama & Nilai")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan (0-4): ")

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            ubah()
        elif pilihan == '3':
            hapus()
        elif pilihan == '4':
            tampilkan()
        elif pilihan == '0':
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Masukkan pilihan antara 0 hingga 4.")

The code enters a loop that continuously displays a menu of options to the user until the user chooses to exit (pilihan == '0').

The menu includes options to add, modify, delete, or display student data.

The user's choice is obtained using input() and processed using conditional statements.

The loop continues until the user chooses to exit (pilihan == '0').