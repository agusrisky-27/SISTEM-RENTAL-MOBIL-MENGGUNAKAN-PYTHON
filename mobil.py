nama_penyewa = ""
no_ktp = 0
jenis_mobil = ""
harga_sewa = 0
lama_sewa = 0

def menu():
    print ("\n=========================")
    print ("         RETAL MOBIL       ")
    print ("=========================\n")

    print ("1. Input Data Rental")
    print ("2. Lihat Data Rental")
    print ("3. Hitung Total Bayar")
    print ("4. Keluar")

def input_data():
    global nama_penyewa
    global no_ktp
    global jenis_mobil
    global harga_sewa
    global lama_sewa

    nama_penyewa = input("Masukan Nama : ")
    no_ktp = int(input("Masukan No KTP : "))
    jenis_mobil = input("Masukan Jenis Mobil : ")
    harga_sewa = int(input("Harga Sewa : "))
    lama_sewa = int(input("Lama Sewa : "))

def lihat_data():
    print ("\n=========================")
    print ("         DATA RENTAL       ")
    print ("=========================\n")

    print ("Nama Penyewa : ", nama_penyewa)
    print ("No. KTP : ", no_ktp)
    print ("Jenis Mobil : ", jenis_mobil)
    print ("Harga Sewa / Hari : ", harga_sewa)
    print ("Lama Sewa : ", lama_sewa)

    print ("")
    print ("=========================")
    print ("")

def total():
    total_sewa = harga_sewa * lama_sewa

    if total_sewa >= 2000000:
        diskon = total_sewa * 15 / 100
    elif total_sewa >= 1000000:
        diskon = total_sewa * 10 / 100
    elif total_sewa >= 500000:
        diskon = total_sewa * 5 / 100
    else:
        diskon = 0
        print ("Tidak Mendapat Diskon")

    total_bayar = total_sewa - diskon
    
    return total_sewa, diskon, total_bayar

jalan = True

while jalan:

    menu()

    pilihan = input("Masukan Pilihan : ")

    if pilihan == "1":
        input_data()

    elif pilihan == "2":
        lihat_data()

    elif pilihan == "3":
        total_sewa, diskon, total_bayar = total()

        print("=========================")
        print("      STRUK RENTAL       ")
        print("=========================")
        print ("Nama Penyewa : ", nama_penyewa)
        print ("Jenis Mobil : ", jenis_mobil)
        print ()
        print ("Harga Sewa / Hari : ", harga_sewa)
        print ("Lama Sewa : ", lama_sewa)
        print ()
        print ("-------------------------\n")
        print ("Total Sewa  :", total_sewa)
        print ("Diskon       :", diskon)
        print ("Total Bayar  :", total_bayar)

    elif pilihan == "4":
        print ("PROGRAM SELESAI")

        jalan = False

    else:
        print ("MENU TIDAK DI TEMUKAN")
    


