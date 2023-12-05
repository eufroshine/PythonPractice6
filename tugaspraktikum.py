# Inisialisasi daftar nilai mahasiswa
daftar_nilai = []

# Fungsi tambah untuk menambah data
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa = {'Nama': nama, 'Nilai': nilai}
    daftar_nilai.append(data_mahasiswa)
    print(f"Data mahasiswa {nama} dengan nilai {nilai} telah ditambahkan.")

# Fungsi tampilkan untuk menampilkan data
def tampilkan():
    if not daftar_nilai:
        print("Daftar nilai mahasiswa kosong.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for data in daftar_nilai:
            print(f"Nama: {data['Nama']}, Nilai: {data['Nilai']}")

# Fungsi hapus untuk menghapus data berdasarkan nama
def hapus():
    nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
    for data in daftar_nilai:
        if data['Nama'] == nama:
            daftar_nilai.remove(data)
            print(f"Data mahasiswa {nama} telah dihapus.")
            return
    print(f"Tidak ditemukan data mahasiswa dengan nama {nama}.")

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
        print("Pilihan tidak valid. Masukkan pilihan antara 0 hingga 5.")