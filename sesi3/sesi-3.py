import random
from libs import selamat_datang

bintang_position = random.randint(1, 4)
selamat_datang( "selamat datang di permainan tebak bintang" )
nama_user = input ("masukan nama anda: ")

while nama_user == "":
        print("Nama tidak boleh kosong")
        nama_user = input ("masukan nama anda: ")
while True:
        Betuk_kotak = "[]"
        kotak  = [Betuk_kotak] * 4
        kotak [bintang_position - 1] = "[*]"
        kotak_kosong = [Betuk_kotak] * 4

        kotak= kotak.copy()     #tempatbaru
        kotak[bintang_position - 1] = "[*]"

        kotak_kosong = '---'.join(kotak_kosong)
        kotak = '---'.join(kotak)
        print(f''' halo {nama_user}! coba  perhatikan kotak di sampig ini 
        {kotak_kosong}    ''')


        #print(kotak)
        #print(f"posisi: {bintang_position}")



        pilih_user = int(input("Menurut kamu icon bintang ada di momor berapa? [1 / 2/ 3/ 4]: "))

        confirm_answer = input(f"Apakah kamu yakin jawaban kamu adalah benar {pilih_user}? [y/n]: ")

        if confirm_answer == "n":
                        print("program di hetikan!")        
                        exit()
        elif confirm_answer == "y": 
                if pilih_user == bintang_position:
                                print(f"{kotak}/n Selamat kamu benar!")
        else:
                                print(f"{kotak}/nMaaf, kamu salah.")

        print("Silahkan ulangi program!")
                
        play_again = input("/n/ apakah ingin melanjutkan program? [y/n]: ")
        if play_again == "n":
                exit()
