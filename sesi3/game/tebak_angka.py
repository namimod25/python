import __main__

from py_compile import main
import random
from tracemalloc import start

while True:
    bintang_position = random.randint(1, 4)
    Betuk_kotak = "[]"
    kotak  = [Betuk_kotak] * 4
    kotak[bintang_position - 1] = "[*]" # type: ignore
    kotak_kosong = [Betuk_kotak] * 4

    kotak= kotak.copy()     #tempatbaru
    kotak[bintang_position - 1] = "[*]" # type: ignore

    kotak_kosong = '---'.join(kotak_kosong)
    kotak = '---'.join(kotak)
    print(f''' halo  coba  perhatikan kotak di sampig ini 
        ''')


        #print(kotak)
        #print(f"posisi: {bintang_position}")



    pilih_user = int(input(f"Menurut kamu icon bintang ada di momor berapa {kotak_kosong} ?  [1 / 2/ 3/ 4]: "))

    confirm_answer = input(f"Apakah kamu yakin jawaban kamu adalah benar {pilih_user}? [y/n]: ")

    if confirm_answer == "n":
                        print("program di hetikan!")        
                        exit()
    elif confirm_answer == "y": 
                if pilih_user == bintang_position: # type: ignore
                                print(f"{kotak}/n Selamat kamu benar!")
    else:
                                print(f"{kotak}/n Maaf, kamu salah.")

    print("Silahkan ulangi program!")
                
    play_again = input("/n/ apakah ingin melanjutkan program? [y/n]: ")
    if play_again == "n":
                print("program di selesai!")
                break
            
    if __main__ == '__main__':
       start()