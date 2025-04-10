import random

bintang_position = random.randint(1, 4)

nama_user = input ("masukan nama anda: ")

print(f'''hallo {nama_user}! coba perhatikan kotak diawah ini
      [] [] [] []
      ''')
pilih_user = int(input("Menurut kamu icon bintang ada di momor berapa? [1 / 2/ 3/ 4]: "))
print(f"pilihan kamu {pilih_user}")

if pilih_user == bintang_position:
        print("Selamat {nama_user}, kamu benar! posisi bintang ada dikotak nomor {bintang_position}, dan pilihan kamu adalah {pilih_user}")
else:
        print(f"Kamu salah posisi bintang bukan disitu! tapi berada di kotak nomor {bintang_position}. dan pilihan kamu adalah {pilih_user}")
        