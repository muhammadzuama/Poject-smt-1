import os
import json
DB_RS='data.json'#nama data jason untuk data base dari yang akan dimasukkan admin

filelogin="signup.json"#data base untuk login
def read() :#fungsi bagian untuk membaca data dari json
    try :
        new_list=[]#list baru untuk tempat dari datannya
        with open(filelogin,'r') as filejason:#'r' di gunakan untuk membaca file jsonnnya
            reader=json.load(filejason)
        for data in reader:
            new_list.append(data)
    except FileNotFoundError:
        new_list=[]
    return new_list
    

def write(newlist):#def berfungsi agar newlist bisa di baca kembali
    with open (filelogin,'w') as filejson:#w berfungsi untuk menulis ke dalam file json
        json.dump(newlist,filejson,indent=4)
def Daftar():#def untuk mengulang pada bagian menu daftar
    print('=== akun baru ===')
    username=input('Masukkan Username :')
    password=input('masukkan password :')
    account={}
    account['Username'] = username
    account['Password'] = password
    if username and password !='':#jika username dan password diisi maka akan dilanjutkan
        new_list=[]#list baru untuk tempat dari data yang akan dibuat
        reader=read()
        if reader != 0:
            for data in reader:
                new_list.append(data)#append berfungsi untuk menambahkan sebuah list ke dalam data
        new_list.append(account)
        write(new_list)
        print('akun berhasil di buat')
        halaman_awal()
    # else:
    
def login():
    reader =read () # memanggil fungsi baca data
    if len(read()) != 0: # mengecek data dalam file username dan password terlebih dahulu
        print('===========================')
        print("======= Masuk ======")
        username = input("Nama Pengguna : ")
        password = input("Kata Sandi : ")
        print('===========================')
        for data in reader: # memanggil data pada file 
            # melakukan pengecekan dengan operan 
            if username == data['Username']:
                if password == data['Password']:
                    print("login Suskses")
                    login_as()
                else: # jika username dan password benar maka akan ditampilkan fitur menu
                    halaman_awal()


#inputan data yang akan di masukkan dan di save di dalam database
def insert(arg1):
    nama = input('Masukkan nama Rumah sakit         :')
    alamat=input('Masukkan Alamat                   :')
    jumlah_dokter_spesialis_dan_umum=input('Jenis Dokter Spesialis yang Tersedia :')
    kapasitas_rumah_sakit=input('Kapasitas Rumah Sakit :')
    jam_beroperasi=input('Jam Operasi Rumah Sakit :')
    arg1.append({#inputan arg1 akan dimasukkan ke dalam variabel dibawah ini
        'Nama Rumah Sakit':nama,
        'Alamat':alamat,
        'Dokter Spesialis':jumlah_dokter_spesialis_dan_umum,
        'Kapasitas Rawat Inap':kapasitas_rumah_sakit,
        'Jam Operasi':jam_beroperasi
    })
    return arg1
#untuk memasukkan ke dalam tampilan
def show(arg1):#untuk membuat tabel dari data arg1 yang telah dimasukkan
    print('|%-2s| %-30s | %-45s | %-40s | %-20s | %-20s |'%('#','NAMA RUMAH SAKIT ','ALAMAT RUMAH SAKIT','DOKTER SPESIALIS','KAPASITAS RUMAH SAKIT','JAM OPERASI'))
    print(158*('='))
    for i in range(len(arg1)):#data yang telah diinputkan dari arg1 akan ditampilkan berupa tabel dengan print seperti dibawah
        print('|%-2s| %-30s | %-45s | %-39s  | %-21s | %-20s |'%(i,arg1[i]['Nama Rumah Sakit'],arg1[i]['Alamat'],arg1[i]['Dokter Spesialis'],arg1[i]['Kapasitas Rawat Inap'],arg1[i]['Jam Operasi']))
#untuk menghapus data
def Delete(arg1):
        indeks=int(input(('pilih indeks yang di happus :')))
        arg1.pop(indeks)#pop adalah fungsi yang digunakan untuk menghapus elemen dalam daftar
        show(arg1)
        return arg1 # fungsi dari return adalah untuk mengembalikan sebuah nilai
#untuk save data
def Save(_datars,_data):
        with open(_datars,'w') as output:#w berfungsi untuk menulis ke dalam file json
            output.write(json.dumps(_data))
        print('=== Save Suksessfull ===')

def load(_path):
    with open(_path,'r')as output:#r berfungsi untuk membaca data dari output 
        if os.stat(_path).st_size==0:
            return[]
        else:
            _data = json.load(output)
            return _data
        
#merupakan tampilan dari menu awal sebelum kita memilih menjadi admin atau user
def menu_awal(arg1):
    print('Selamat datang di Aplikasi Data Informasi Rumah sakit ')
    print('====================================')
    print('[1] Daftar')
    print('[2] Login')
    print('[0] Keluar')
    print('=====================================')
    return arg1

#merupakan tampilan setelah kita masuk menjadi admin
def menu(arg1):
    print('===== MENU ADMIN =====')
    print('[1] Lihat data')
    print('[2] Tambah Data')
    print('[3] Save Data')
    print('[4] Hapus Data')
    print('[0] Keluar')
    print('-'*20) #pembatas agar nantinya tampilan lebih menarik begitu juga dengan =
    print('=========================')
    return(arg1)
#menu sebagai admin
def menu_sampingan ():
    os.system('cls')#untuk menghapus program sebelumnya agar terlihat lebih rapi
    data=load(DB_RS)#untuk memangil data yang telah tersimpan di json
    while True:
        print(menu(arg1=''))
        pilihan_menu = input('Pilih menu: ')
        if pilihan_menu == '1': #pilihan 1 untuk melihat data yang telah di isi
            show(data)  
        elif pilihan_menu == '2': #pilihan 2 untuk menambah data rumah sakit
            data=insert(data)
            os.system('cls')
        elif pilihan_menu == '3' : #pilihan 3 untuk menyimpan data yang di isi
            Save(DB_RS,data)
        elif pilihan_menu == '4' : #pilihan 4 untuk hapus data melalui indeks #
            data=Delete(data)
        elif pilihan_menu == '0' : #pilihan 0 untuk keluar dari aplikasi
            os.system('cls')
            tanya = input("Tekan enter untuk keluar..., Tekan (n) untuk kembali... ") # mengkonfirmasi apakah users benar benar ingin keluar dari aplikasi
            if (tanya == "n") or (tanya == "N"): # kemudian membuat operand untuk keluar
                os.system('cls')#untuk menghapus halaman sebelumnnya
            else:
                os.system('cls')#untuk menghapus halaman sebelumnnya
                halaman_awal()#untuk kembali ke menu awal

def login_as():
    w=input('Login sebagai admin/user =')
    if w=='admin':#Jika memilih admin maka akan menuju menuju menu_sampingan
        menu_sampingan()
    elif w=='ADMIN' :#Jika memilih ADMIN maka akan menuju menuju menu_sampingan
        menu_sampingan()
    elif w=='user' :#Jika memilih user maka akan menuju menuju menu_sampingan
        userface()
    elif w=='USER' :#Jika memilih USER maka akan menuju menuju menu_sampingan
        userface()
    else: # jika tidak menginputkan sesuai ketentuan maka akan kembali ke halaman awal
        halaman_awal()

# tampilan ketika kita memilih login sebagai admin
def pengguna(arg1):
    print('===== MENU USER =====')
    print('[1] Lihat data')
    print('[2] Quit')
    print('======================')
    return arg1

def userface():
    os.system('cls')#untuk menghapus halaman sebelumnnya
    data=load(DB_RS)
    while True :
        print(pengguna(arg1=''))
        choise=input('Pilih = ')
        if choise=='1': # jika memilih satu akan menampilkan data
            show(data)#untuk menampilkan data atau tabel data yang
        elif choise=='2':# jika memilih dua akan keluar dari halaman user
            os.system('cls')#untuk menghapus halaman sebelumnnya
            tanya = input("Tekan enter untuk keluar..., Tekan (n) untuk kembali... ") # mengkonfirmasi apakah users benar benar ingin keluar dari aplikasi
            if (tanya == "n") or (tanya == "N"): # kemudian membuat operand untuk keluar
                os.system('cls')#untuk menghapus halaman sebelumnnya
            else:
                #untuk menghapus halaman sebelumnnya
                halaman_awal()#untuk kembali ke menu awal


def halaman_awal():#fungsi dari menu utama
    os.system('cls')#untuk membersihkan dari program sebelumnya
    while True :#perulangan untuk selalu bisa menampilkan dan menjalankan menu 
        print(menu_awal(arg1=''))
        choise=input('Pilih = ')
        if choise=='1':
            Daftar()#langsung masuk pada fungsi daftar
        elif choise=='2':
            login()#langsung masuk ke dalamn dhalaman login
        elif choise == '0':#pilihan jika ingin keluar dari program
            os.system('cls')#untuk menghapus halaman sebelumnnya
            tanya = input("Tekan enter untuk keluar..., Tekan (n) untuk kembali... ") # mengkonfirmasi apakah users benar benar ingin keluar dari aplikasi
            if (tanya == "n") or (tanya == "N"): # kemudian membuat operand untuk keluar
                os.system('cls')#untuk menghapus halaman sebelumnnya
            else:
                os.system('cls')#untuk menghapus halaman sebelumnnya
                exit()#unruk keluar dari aplikasi
halaman_awal()#untuk memanggil semua sintaks