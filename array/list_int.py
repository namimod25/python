import random

# Array dengan 1000 angka acak (integer) antara 1 dan 1000
array = [random.randint(1, 1000) for _ in range(50)]

# Jika Anda ingin melihat sebagian datanya
print(array[:10])  # Menampilkan 10 elemen pertamas