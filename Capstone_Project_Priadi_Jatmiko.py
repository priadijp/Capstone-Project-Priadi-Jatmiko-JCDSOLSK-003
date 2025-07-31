#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ======================================== #
#  PROGRAM RENTAL MOBIL                    #
#  PRIADI JATMIKO                          #
#  KELAS DATA SCIENCE -- JCDSOLSK-003      #
# ======================================== #

# Dummy untuk mempermudah uji coba lihat data mobil, ubah data mobil, hapus data mobil, sewa/kembalikan mobil 

# {nopol_mobil, nama_mobil, jumlah_kursi, harga_sewa, tersedia, tahun_mobil, pemilik}
# Default Tersedia = Ada, agar data sewa dimasukkan melalui MENU SEWA

data_mobil = {
    "B 1111 AA": {"nama_mobil": "VELOZ", "jumlah_kursi": 6, "harga_sewa": 400000, "tersedia": "Ada", "tahun_mobil": 2023, "pemilik": "ALAN"},
    "B 2222 BB": {"nama_mobil": "INNOVA ZENIX", "jumlah_kursi": 6, "harga_sewa": 600000, "tersedia": "Ada", "tahun_mobil": 2025, "pemilik": "DORA"},
    "B 3333 CC": {"nama_mobil": "PAJERO SPORT", "jumlah_kursi": 7, "harga_sewa": 800000, "tersedia": "Ada", "tahun_mobil": 2023, "pemilik": "LISA"},
    "B 4444 DD": {"nama_mobil": "FORTUNER", "jumlah_kursi": 7, "harga_sewa": 800000, "tersedia": "Ada", "tahun_mobil": 2024, "pemilik": "VELTHOM"}
}

# {nopol_mobil, nama_mobil, penyewa, tanggal_sewa, tanggal_kembali, harga_sewa, total_harga}
data_sewa = {}
                  
# === FUNGSI MENU DAN SUB MENU ===

# Menu Utama Rental Mobil
def menu_utama():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'***   MENU UTAMA   ***':^40}")
    print("=" * 40)
    print("   1. Isi Data Mobil")
    print("   2. Lihat Data Mobil")
    print("   3. Ubah Data Mobil")
    print("   4. Hapus Data Mobil")
    print("   5. Sewa/Kembalikan Mobil")
    print("   6. Keluar Menu")
    print("-" * 40)

# 1. Sub Menu Isi Data Mobil
def menu_isi_data():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'**   MENU ISI DATA MOBIL   **':^40}")
    print("=" * 40)
    print("   1. Isi Rincian Data Mobil")
    print("   2. Kembali ke Menu Utama")
    print("-" * 40)

# 2. Sub Menu Lihat Data Mobil
def menu_lihat_data():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'**   MENU LIHAT DATA MOBIL   **':^40}")
    print("=" * 40)
    print("   1. Lihat Daftar Mobil")
    print("   2. Lihat Rincian Data Mobil")
    print("   3. Kembali ke Menu Utama")
    print("-" * 40)

# 3.a. Sub Menu Ubah Data Mobil
def menu_ubah():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'**   MENU UBAH DATA MOBIL   **':^40}")
    print("=" * 40)
    print("   1. Ubah Rincian Data Mobil")
    print("   2. Kembali ke Menu Utama")
    print("-" * 40)

# 3.b. Sub Menu Ubah Rincian Data Mobil
def menu_ubah_rincian():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'*   MENU UBAH RINCIAN DATA MOBIL   *':^40}")
    print("=" * 40)
    print("   1. Ubah Nama Mobil")
    print("   2. Ubah Jumlah Kursi")
    print("   3. Ubah Harga Sewa")
    print("   4. Ubah Ketersediaan Mobil")
    print("   5. Ubah Tahun Mobil")
    print("   6. Ubah Nama Pemilik Mobil")
    print("   7. Kembali ke Menu Ubah Data Mobil")
    print("-" * 40)

# 4. Sub Menu Hapus Data Mobil
def menu_hapus():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'**   MENU HAPUS DATA MOBIL   **':^40}")
    print("=" * 40)
    print("   1. Hapus Data Mobil")
    print("   2. Kembali ke Menu Utama")
    print("-" * 40)

# 5. Sub Menu Sewa/Kembalikan Mobil
def menu_sewa():
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("-" * 40)
    print(f"{'**   MENU SEWA/KEMBALIKAN MOBIL   **':^40}")
    print("=" * 40)
    print("   1. Sewa Mobil")
    print("   2. Kembalikan Mobil")
    print("   3. Kembali ke Menu Utama")
    print("-" * 40)


# Fungsi Tampilkan Data Mobil -- digunakan oleh Fungsi : Lihat Data Mobil, Ubah Data Mobil, Hapus Data Mobil, Sewa Mobil
# (status Ada = Tersedia, Sewa = Tersewa, None = semua Data Mobil)

def tampilkan_data(status=None):   # default status = None
 
    # Inisialisasi untuk menampilkan nomor urut
    no_index = 1
    
    # Penamaan judul sesuai status mobil
    if status == 'Ada':
        judul = 'TERSEDIA'
    elif status == 'Sewa':
        judul = 'TERSEWA'
    else:
        judul = 'SEMUA'

    # Tampilkan Daftar Mobil yang Tersedia/Tersewa/Semua Mobil
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print(f"{f'DAFTAR MOBIL {judul}':^82}")    # menggunakan 2 format: tengah dan status judul
    print("-" * 82)
    print(f"{'No':^4} | {'Nomor Polisi':^12} | {'Nama Mobil':^18} | {'Jumlah Kursi':^12} | {'Harga Sewa':^12} | {'Tersedia':^8}")        
    print("=" * 82)        
    
    for nopol_mobil, mobil in data_mobil.items():     
        if status is None or mobil['tersedia'] == status:
            print(f"{no_index:^4} | {nopol_mobil:<12} | {mobil['nama_mobil']:<18} | {mobil['jumlah_kursi']:^12} | {mobil['harga_sewa']:>12.2f} | {mobil['tersedia']:^8}")
            no_index += 1
    print("-" * 82)


# Fungsi Tampilkan Rincian Data Mobil sesuai masukan key -- digunakan oleh Fungsi: Lihat Data Mobil, Ubah Data Mobil, Hapus Data Mobil, Sewa Mobil
def rincian_mobil(nopol_mobil):      
    print(f" {'Nama Mobil':<40} : {data_mobil[nopol_mobil]['nama_mobil']}")
    print(f" {'Jumlah Kursi Penumpang':<40} : {data_mobil[nopol_mobil]['jumlah_kursi']}")
    print(f" {'Harga Sewa Mobil 1 Hari':<40} : {data_mobil[nopol_mobil]['harga_sewa']:.2f}")
    print(f" {'Ketersediaan Mobil':<40} : {data_mobil[nopol_mobil]['tersedia']}")
    print(f" {'Tahun Mobil':<40} : {data_mobil[nopol_mobil]['tahun_mobil']}")
    print(f" {'Nama Pemilik Mobil':<40} : {data_mobil[nopol_mobil]['pemilik']}")
    print("-" * 60)

# Fungsi Tampilkan Daftar Mobil yang Tersewa - digunakan oleh Fungsi: Pembayaran, Kembalikan Mobil
def tampilkan_sewa():   # default status = Sewa
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print(f"{'DAFTAR MOBIL TERSEWA':^140}")
    print("-" * 140)
    print(f"{'No':^4} | {'Nomor Polisi':^12} | {'Nama Mobil':^18} | {'Nama Penyewa':^20} | {'Tanggal Sewa':^12} | {'Tanggal Kembali':^15} | {'Lama Sewa':^10} | {'Harga Sewa':^12} | {'Total Harga':^12}")        
    print("=" * 140)
    
    no_index = 1

    for nopol_mobil, mobil in data_sewa.items():
        print(f"{no_index:^4} | {nopol_mobil:<12} | {mobil['nama_mobil']:<18} | {mobil['penyewa']:<20} | {mobil['tanggal_sewa']:^12} | {mobil['tanggal_kembali']:^15} | {str(mobil['lama_sewa']) + ' Hari':^10} | {mobil['harga_sewa']:>12.2f} | {mobil['total_harga']:>12.2f}")
        no_index += 1
    print("-" * 140)


# Fungsi Tampilkan Rincian Data Sewa sesuai masukan key -- digunakan oleh Fungsi: Kembalikan Mobil
def rincian_sewa(nopol_mobil):      
    print(f" {'Nama Mobil':<40} : {data_sewa[nopol_mobil]['nama_mobil']}")
    print(f" {'Nama Penyewa':<40} : {data_sewa[nopol_mobil]['penyewa']}")
    print(f" {'Tanggal Sewa':<40} : {data_sewa[nopol_mobil]['tanggal_sewa']}")
    print(f" {'Tanggal Kembali':<40} : {data_sewa[nopol_mobil]['tanggal_kembali']}")
    print(f" {'Lama Sewa':<40} : {str(data_sewa[nopol_mobil]['lama_sewa']) + ' Hari'}")
    print(f" {'Harga Sewa Mobil':<40} : {data_sewa[nopol_mobil]['harga_sewa']:.2f}")
    print(f" {'Total Harga':<40} : {data_sewa[nopol_mobil]['total_harga']:.2f}")
    print("-" * 60)


# Fungsi Pembayaran Sewa Mobil
def pembayaran(penyewa, total_harga):

    tampilkan_sewa()   # Tampilkan Daftar Mobil Tersewa

    # Validasi jumlah pembayaran
    while True:
        print()
        bayar_sewa = int(input(f"{'Masukkan jumlah uang pembayaran':<40} : "))
        if bayar_sewa > total_harga:
            kembalian = bayar_sewa - total_harga
            print()
            print(f"{f'Uang kembalian Anda':<40} : {kembalian:.2f}")
            print()
            print("*** Terima kasih. Semoga sehat salalu ***")
            break;   # Kembali ke Menu Sewa Mobil
        elif bayar_sewa == total_harga:
            print()
            print("*** Terima kasih. Utamakan Selamat ***")
            break;   # Kembali ke Menu Sewa Mobil
        else:
            kurang_bayar = total_harga - bayar_sewa
            print(f"{f'Maaf uang pembayaran kurang':<40} : {kurang_bayar:.2f}")
            continue;
    
    # Cetak Tanda Terima Pembayaran/Invoice
    print()
    print("RENTAL MOBIL VELTHOM")
    print(tanggal_sekarang)
    print()
    print("Kepada Yth.")
    print(f"Bapak/Ibu/Sdr. {penyewa}")
    print()
    print(f"{'TANDA TERIMA PEMBAYARAN':^140}")
    print("-" * 140)
    print(f"{'No':^4} | {'Nomor Polisi':^12} | {'Nama Mobil':^18} | {'Nama Penyewa':^20} | {'Tanggal Sewa':^12} | {'Tanggal Kembali':^15} | {'Lama Sewa':^10} | {'Harga Sewa':^12} | {'Total Harga':^12}")        
    print("=" * 140)
    
    no_index = 1

    for nopol_mobil, mobil in data_sewa.items():
        print(f"{no_index:^4} | {nopol_mobil:<12} | {mobil['nama_mobil']:<18} | {mobil['penyewa']:<20} | {mobil['tanggal_sewa']:^12} | {mobil['tanggal_kembali']:^15} | {str(mobil['lama_sewa']) + ' Hari':^10} | {mobil['harga_sewa']:>12.2f} | {mobil['total_harga']:>12.2f}")
        no_index += 1
    print("-" * 140)
    
    print(f"{'Jumlah Dibayar'} {total_harga:>124.2f}")
    print("-" * 140)
    print()
    print("PEMBAYARAN LUNAS. TERIMA KASIH")
    print()
    print("  ttd")
    print()
    print("VELTHOM")
    return;


# Fungsi Isi Data Mobil
def isi_data():
    
    while True:
        
        menu_isi_data()   # Tampilkan Menu Isi Data Mobil

        pilihan = input("Pilihan Menu (1-2) : ")

        if pilihan.isdigit():   # Apakah data yang dimasukkan berupa angka?

            if pilihan == '1':                
                print()
                print("RENTAL MOBIL VELTHOM")
                print(tanggal_sekarang)
                print()
                print(f"{'ISI RINCIAN DATA MOBIL':^60}")
                print("=" * 60)
                
                nopol_mobil = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()
                
                # Apakah No Polisi mobil ada dalam data mobil?
                if nopol_mobil in data_mobil:     
                    print()
                    print("*** Data mobil sudah ada ***")
                else:    
                    nama_mobil = input(f" {'Masukkan Nama Mobil':<40} : ").upper()
                    jumlah_kursi = input(f" {'Masukkan Jumlah Kursi Penumpang':<40} : ")
                    harga_sewa = float(input(f" {'Masukkan Harga Sewa Mobil 1 Hari':<40} : "))
                    tahun_mobil = int(input(f" {'Masukkan Tahun Mobil ':<40} : "))
                    pemilik = input(f" {'Masukkan Nama Pemilik Mobil ':<40} : ").upper()
                    print("-" * 60)
                    
                    # Validasi masukan (y/t)
                    while True:                        
                        simpan = input("Apakah data akan disimpan? (y/t) : ").lower()                
                        
                        if simpan.lower() == 'y':   # Simpan Data Mobil
                            data_mobil[nopol_mobil] = {     
                                "nama_mobil": nama_mobil,
                                "jumlah_kursi": jumlah_kursi,
                                "harga_sewa": harga_sewa,
                                "tersedia": 'Ada',
                                "tahun_mobil": tahun_mobil,
                                "pemilik": pemilik
                            }
                            print()
                            print("*** Data berhasil disimpan ***")
                            print()
                            break;
                        elif simpan.lower() == 't':
                            break;

            # Kembali ke Menu Utama Rental Mobil
            elif pilihan == '2':
                return;    
            else:   # Jika angka yang dimasukkan bukan (1-2)
                print()
                print("*** Harap masukkan angka (1-2) ***")

        else:   # Jika masukan bukan berupa angka
            print()
            print("*** Pilihan yang Anda masukkan bukan angka ***")


# Fungsi Lihat Data Mobil
def lihat_data():     

    while True:
    
        menu_lihat_data()   # Tampilkan Menu Lihat Data Mobil

        pilihan = input("Pilihan Menu (1-3) : ")

        if pilihan.isdigit():   # Apakah data yang dimasukkan berupa angka 
            
            # Lihat Data Mobil
            if pilihan == '1':
            
                if not data_mobil:   # Apakah sudah ada data mobil?
                    print()
                    print("*** Data mobil masih kosong. Silahkan isi data ***")
                else:
                    tampilkan_data()   # status = None, tampilkan Daftar Mobil Semua
            
            # Tampilkan Rincian Data Mobil
            elif pilihan == '2':       
                
                if not data_mobil:   # Apakah sudah ada data mobil?
                    print()
                    print("*** Data mobil masih kosong. Silahkan isi data ***")
                else:
                    print()
                    print("RENTAL MOBIL VELTHOM")
                    print(tanggal_sekarang)
                    print()
                    print(f"{'LIHAT RINCIAN DATA MOBIL':^60}")
                    print("=" * 60)          
                    
                    nopol = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()              
                
                    if nopol in data_mobil:   # Apakah key yang dimasukkan ada dalam data?

                        rincian_mobil(nopol)   # Tampilkan Rincian Data Mobil sesuai key
                    
                    else:
                        print()
                        print("*** Data mobil tidak ada ***")

            # Kembali ke Menu Utama
            elif pilihan == '3':     
                return;    
            else:   # Jika masukan angka tidak sesuai, kembali ke Menu Lihat Data Mobil
                print()
                print("*** Harap masukkan angka (1-3) ***")

        else:   # Jika masukkan bukan berupa angka, kembali ke Menu Lihat Data Mobil
            print()
            print("*** Pilihan yang Anda masukkan bukan angka ***")


# Fungsi Ubah Data Mobil
def ubah_data():                   
    
    while True:

        if not data_mobil:   # Apakah sudah ada data mobil?
            print()
            print("*** Data mobil masih kosong. Silahkan isi data ***")
            return;
            
        menu_ubah()   # Tampilkan Menu Ubah Data Mobil

        pilihan = input("Pilihan Menu (1-2) : ")

        if pilihan.isdigit():   # Apakah data yang dimasukkan berupa angka 
            
            # Ubah Data Mobil
            if pilihan == '1':                
                
                tampilkan_data()   # Tampilkan dahulu semua Data Mobil
                
                print()
                print("RENTAL MOBIL VELTHOM")
                print(tanggal_sekarang)
                print()
                print(f"{'UBAH RINCIAN DATA MOBIL':^60}")
                print("=" * 60)
                
                nopol = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()               
                
                if nopol not in data_mobil:   # Apakah key yang dimasukkan ada dalam data?                    
                    print()
                    print("*** Data mobil tidak ada ***")
                    continue;   # Kembali ke Menu Ubah Data Mobil
                    
                rincian_mobil(nopol)   # Tampilkan Rincian Data Mobil sesuai key
                
                # Validasi masukan (y/t)
                while True:                       
                    lanjut = input("Apakah data akan diubah? (y/t) : ").lower()                        
                    if lanjut.lower() == 'y' or lanjut.lower() == 't':
                        break;   # Keluar dari while, lanjut ke perintah berikutnya

                if lanjut.lower() == 't':
                    continue;   # Kembali ke Menu Ubah Data Mobil
                    
                menu_ubah_rincian()   # Tampilkan Menu Ubah Rincian Data Mobil

                pilih_ubah = input("Pilihan Menu (1-7) : ")

                if pilih_ubah.isdigit():   # Apakah data yang dimasukkan berupa angka

                    # "kolom" adalah key atribut, "data_baru" adalah data yang akan disimpan
                    if pilih_ubah == '1':
                        nama_mobil = input(f" {'Masukkan Nama Mobil':<40} : ").upper()
                        kolom = 'nama_mobil'
                        data_baru = nama_mobil                                    
                    elif pilih_ubah == '2':
                        jumlah_kursi = input(f" {'Masukkan Jumlah Kursi Penumpang':<40} : ")
                        kolom = 'jumlah_kursi'
                        data_baru = jumlah_kursi                                    
                    elif pilih_ubah == '3':
                        harga_sewa = float(input(f" {'Masukkan Harga Sewa Mobil 1 Hari':<40} : "))
                        kolom = 'harga_sewa'
                        data_baru = harga_sewa                                   
                    elif pilih_ubah == '4':
                        tersedia = input(f" {'Masukkan Ketersediaan Mobil (Ada/Sewa)':<40} : ").title()
                        kolom = 'tersedia'
                        data_baru = tersedia
                    elif pilih_ubah == '5':
                        tahun_mobil = int(input(f" {'Masukkan Tahun Mobil':<40} : "))
                        kolom = 'tahun_mobil'
                        data_baru = tahun_mobil                                   
                    elif pilih_ubah == '6':
                        pemilik = input(f" {'Masukkan Nama Pemilik Mobil':<40} : ").upper()
                        kolom = 'pemilik'
                        data_baru = pemilik                               
                    elif pilih_ubah == '7':
                        lanjut = 't'
                        break;   # Kembali ke Menu Ubah Data Mobil                      
                    else:
                        lanjut = 't'
                        print()
                        print("*** Harap masukkan angka (1-7) ***")
                        print()                                 
                else:
                    print()
                    print("*** Pilihan yang Anda masukkan bukan angka ***")
                    print()

                # Jika data jadi diubah            
                while lanjut.lower() == 'y':                        

                    ubah = input("Apakah data yang diubah akan disimpan? (y/t) : ").lower()

                    if ubah.lower() == 'y':
                        data_mobil[nopol][kolom] = data_baru   # Simpan data yang baru
                        print()
                        print("*** Data berhasil diubah ***")
                        print()
                        break;   # Berhasil ubah data, kembali ke Menu Ubah Data Mobil
                    elif ubah.lower() == 't':
                        break;   # Batal ubah data, kembali ke Menu Ubah Data Mobil

            # Kembali ke Menu Utama                   
            elif pilihan == '2':
                return;
            else:   # Jika masukan angka tidak sesuai, kembali ke Menu Ubah Data Mobil
                print()
                print("*** Harap masukkan angka (1-2) ***")
                print()
        else:   # Jika masukkan bukan berupa angka, kembali ke Menu Ubah Data Mobil
            print()
            print("*** Pilihan yang Anda masukkan bukan angka ***")
            print()


# Fungsi Hapus Data Mobil
def hapus_data():
    
    while True:
        
        if not data_mobil:   # Apakah sudah ada data mobil?
            print()
            print("*** Data mobil masih kosong. Silahkan isi data ***")
            print()
            return;   # Kembali ke Menu Utama Rental Mobil
            
        menu_hapus()   # Tampilkan Menu Hapus Data Mobil

        pilihan = input("Pilihan Menu (1-2) : ")

        if pilihan.isdigit():   # Apakah data yang dimasukkan berupa angka

            if pilihan == '1':

                tampilkan_data()   # Tampilkan dahulu semua Data Mobil
                
                print()
                print("RENTAL MOBIL VELTHOM")
                print(tanggal_sekarang)
                print()
                print(f"{'HAPUS DATA MOBIL':^60}")
                print("=" * 60)
                
                nopol = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()               
                
                if nopol not in data_mobil:   # Apakah key yang dimasukkan ada dalam data?
                    print()
                    print("*** Data mobil tidak ada ***")
                    print()
                    continue;   # Kembali ke Menu Hapus Data Mobil

                elif data_mobil[nopol]['tersedia'] == 'Sewa':
                    print()
                    print("*** Status mobil masih tersewa ***")
                    print()
                    continue;   # Kembali ke Menu Hapus Data Mobil

                rincian_mobil(nopol)   # Tampilkan Rincian Data Mobil

                # Validasi masukan (y/t)
                while True:                        
                    hapus = input("Apakah data akan dihapus? (y/t) : ").lower()

                    if hapus.lower() == 'y':
                        del data_mobil[nopol]   # Hapus data mobil
                        print()
                        print("*** Data berhasil dihapus ***")
                        print()
                        break;   # Kembali ke Menu Hapus Data Mobil
                        
                    elif hapus.lower() == 't':
                        break;   # Batal hapus data, Kembali ke Menu Hapus Data Mobil
            
            # Kembali ke Menu Utama
            elif pilihan == '2':
                return;    
            else:   # Jika masukan angka tidak sesuai, kembali ke Menu Hapus Data Mobil
                print()
                print("*** Harap masukkan angka (1-2) ***")
                print()

        else:   # Jika masukkan bukan berupa angka, kembali ke Menu Hapus Data Mobil
            print()
            print("*** Pilihan yang Anda masukkan bukan angka ***")
            print()


# Fungsi Sewa/Kembalikan Mobil
def sewa_mobil():        
    
    while True:

        menu_sewa()   # Tampilkan Menu Sewa Mobil

        pilihan = input("Pilihan Menu (1-3) : ")

        if pilihan.isdigit():   # Apakah data yang dimasukkan berupa angka
            
            # Sewa Mobil
            if pilihan == '1':
                
                tagihan = 0

                while True:
                    
                    tampilkan_data('Ada')   # Tampilkan data mobil yang tersedia

                    print()
                    print("RENTAL MOBIL VELTHOM")
                    print(tanggal_sekarang)
                    print()
                    print(f"{'SEWA MOBIL':^60}")
                    print("=" * 60)   
                
                    nopol = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()               

                    if nopol not in data_mobil:   # Apakah key yang dimasukkan ada dalam data?
                        print()
                        print("*** Data mobil tidak ada ***")
                        print() 
                        continue;   # Kembali ke Menu Sewa Mobil
                    elif data_mobil[nopol]['tersedia'] == 'Sewa':
                        print()
                        print("*** Mobil telah tersewa ***")
                        print()
                        continue;   # Kembali ke Menu Sewa Mobil
                
                    rincian_mobil(nopol)   # Tampilkan Rincian Data Mobil
                
                    # Validasi masukan (y/t)
                    while True:
                    
                        sewa = input("Apakah mobil akan disewa? (y/t) : ").lower()
                        print()

                        if sewa.lower() == 'y':
                            break;   # Keluar dari while, lanjut ke perintah berikutnya
                        elif sewa.lower() == 't':
                            break;
                            
                    if sewa.lower() == 'y':
                        
                        penyewa = input(f" {'Masukkan Nama Penyewa':<40} : ").upper()
                        tanggal_kembali = input(f" {'Masukkan tanggal kembali (dd-mm-yyyy)':<40} : ")     
                        lama_sewa = int(input(f" {'Masukkan lama sewa (hari)':<40} : "))

                        tanggal_sewa = tanggal_sekarang
                        total_harga = data_mobil[nopol]['harga_sewa'] * lama_sewa
                    
                        print(f" {'Harga Sewa Mobil 1 Hari':<40} : {data_mobil[nopol]['harga_sewa']:.2f} ")
                        print(f" {'Total Harga':<40} : {total_harga:.2f}")

                        data_sewa[nopol] = {   # Simpan data mobil yang disewa
                            "nama_mobil": data_mobil[nopol]['nama_mobil'],
                            "penyewa": penyewa,
                            "tanggal_sewa": tanggal_sewa,
                            "tanggal_kembali": tanggal_kembali,
                            "lama_sewa": lama_sewa,
                            "harga_sewa": data_mobil[nopol]['harga_sewa'],
                            "total_harga": total_harga
                        }                           
                        data_mobil[nopol]['tersedia'] = 'Sewa'   # Ubah status mobil yang tersewa
                     
                        print()
                        print("*** Data berhasil disimpan ***")
                        print()

                        pembayaran(penyewa, total_harga)   # Pembayaran Sewa, kirim penyewa dan total_harga
                        break;
                    else:
                        break;
            
            # Kembalikan mobil yang disewa
            elif pilihan == '2':                                  
                
                if not data_sewa:   # Apakah sudah ada data mobil?
                    print()
                    print("*** Belum ada mobil tersewa ***")
                    continue;   # Kembali ke Menu Sewa Mobil             

                while True:
                    
                    tampilkan_sewa()   # Tampilkan data mobil yang tersewa

                    print()
                    print("RENTAL MOBIL VELTHOM")
                    print(tanggal_sekarang)
                    print()
                    print(f"{'KEMBALIKAN MOBIL':^60}")
                    print("=" * 60)
                
                    nopol = input(f" {'Masukkan Nomor Polisi Mobil':<40} : ").upper()

                    if nopol not in data_sewa:   # Apakah key yang dimasukkan ada dalam data?
                        print()
                        print("*** Data mobil tidak ada ***")
                        print() 
                        continue;   # Kembali ke Tampilkan Data Mobil Tersewa
                    else:
                        break;

                rincian_sewa(nopol)   # Tampilkan Rincian Data Mobil

                # Validasi masukan (y/t)
                while True:
                    kembalikan_mobil = input("Mobil akan dikembalikan? (y/t) : ").lower()

                    if kembalikan_mobil.lower() == 'y':
                        print()
                        print("*** Terima kasih. Semoga anda sehat selalu ***")
                        print()
                        del data_sewa[nopol]   # Hapus Data Sewa Mobil tersebut
                        
                        data_mobil[nopol]['tersedia'] = 'Ada'   # Kembalikan status mobil menjadi Tersedia
                        break;   # Kembali ke Menu Sewa Mobil

                    elif kembalikan_mobil.lower() == 't':
                        break;   # Batal kembalikan mobil, Kembali ke Menu Sewa Mobil

            # Kembali ke Menu Utama Rental Mobil
            elif pilihan == '3':
                return;    

            else:   # Jika masukan angka tidak sesuai, kembali ke Menu Sewa Mobil
                print()
                print("*** Harap masukkan angka (1-3) ***")
                print()

        else:   # Jika masukkan bukan berupa angka, kembali ke Menu Sewa Mobil
            print()
            print("*** Pilihan yang Anda masukkan bukan angka ***")
            print()


# ==================================
#     PROGRAM UTAMA RENTAL MOBIL
# ==================================

# Diawali dengan memasukkan tanggal sekarang untuk sewa mobil

tanggal_sekarang = input("Masukkan tanggal sekarang (dd-mm-yyyy) : ")

while True:

    # Menjalankan Menu Utama Rental Mobil
    menu_utama()  
    
    pilih = input("Pilihan Menu (1-6):")

    if pilih.isdigit():   # Validasi masukan berupa angka 
        
        if pilih == '1':   # Menjalankan Menu Isi Data Mobil
            isi_data()
        elif pilih == '2':   # Menjalankan Menu Lihat Daftar Mobil
            lihat_data()
        elif pilih == '3':   # Menjalankan Menu Ubah Data Mobil
            ubah_data()
        elif pilih == '4':   # Menjalankan Menu Hapus Data Mobil
            hapus_data()
        elif pilih == '5':   # Menjalankan Menu Sewa/Kembalikan Mobil
            sewa_mobil()
        elif pilih == '6':   # Menjalankan Keluar Menu Utama
            print()
            print("*** Anda sudah keluar dari Menu Utama. Terima kasih ***")
            print()
            break;
        else:        # Jika angka masukkan diluar (1-6), kembali ke Menu Utama Rental Mobil
            print()             
            print("*** Harap masukkan angka (1-6) ***")
            print()    

    else:        # Jika masukan bukan berupa angka, kembali ke Menu Utama Rental Mobil
        print()                 
        print("*** Pilihan yang Anda masukkan bukan angka ***")
        print()

        
# =================================
#           AKHIR PROGRAM
# =================================


# In[ ]:




