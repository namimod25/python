from tracemalloc import start
from libs import selamat_datang
from game import tebak_angka

def main():
        selamat_datang("selamat datang di permainan tebak bintang")
        tebak_angka.start()
if __name__ == "__main__":
       main()