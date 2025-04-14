import random

bintang_position = random.randint(1, 4)

nama_user = input ("masukan nama anda: ")

Betuk_kotak = "[]"
kotak  = [Betuk_kotak] * 4
kotak [bintang_position - 1] = "[*]"
kotak_kosong = [Betuk_kotak] * 4
kotak= kotak.copy()     #tempatbaru
kotak[bintang_position - 1] = "[*]"


print(f''' halo {nama_user}! coba  perhatikan kotak di sampig ini {kotak}
        ''')


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
        
        
        
        