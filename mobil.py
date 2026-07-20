nama penyewa = ""
no_ktp = 0
jenis_mobil = ""
harga_sewa = 0
lama_sewa = 0

def input_data()
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

def lihat_data()
    print("\n=========================")
    print("         DATA RENTAL       ")
    print("=========================\n")

    print ("Nama Penyewa : ", nama_penyewa)
    print ("No. KTP : ", no_ktp)
    print ("Jenis Mobil : ", jenis_mobil)
    print ("JHarga Sewa / Hari : ", harga_sewa)
    print ("Lama Sewa : ", lama_sewa)

    print("")
    print("=========================")
    print("")



