nama = "Nami"
usia = 26
nomor_hp = "08123456789"
print("----------------------------------------------------")
print(f'''nama saya {nama} dan saya berusia {usia} tahun''',f''' nomor_hp saya adalah {nomor_hp}''')
print("----------------------------------------------------")

if nomor_hp ==  usia and usia == 26:
    print("kalau usia dan momor hp sesuai dengan data diatas berarti saya")
else:
    print("kalau usia saya tidak sesuai dengan data diatas berarti bukan saya")
    if nomor_hp == 0:
        print("kalau nomer hp saya sesuai dengan data diatas berarti saya")
    else:
        print("kalau nomor hp saya tidak sesuai dengan data diatas berarti bukan saya")