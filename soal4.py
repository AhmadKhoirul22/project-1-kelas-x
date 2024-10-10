def cari_nilai(a,b):
    if a == 0:
        return "nilai a tidak boleh 0"
    x = -b / a
    # kenapa bisa x = -b / a karena ax + b = 0, seperti pada soal
    return x

a = int(input("masukan nilai a : "))
b = int(input("masukan nilai b : "))
hasil = cari_nilai(a,b)
print(hasil)