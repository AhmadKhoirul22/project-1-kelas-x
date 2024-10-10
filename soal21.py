def angka_ganjil(angka):
    ganjil = [angka for angka in angka if angka % 2 != 0]
    return ganjil

angka = [1,2,3,4,5,6,7,8,9]
hasil = angka_ganjil(angka)
print(hasil)