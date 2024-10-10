# soal 1
import statistics
def hitung_rata_rata(data):
    rata_rata = statistics.mean(data)
    return rata_rata

data = [9, 12, 3, 14, 7]
hasil = hitung_rata_rata(data)
print("Rata-rata dari data", data, "adalah", hasil)
# soal 2
def hitung_nilai_tengah(data):
    nilai_tengah = statistics.median(data)
    return nilai_tengah

data = [9, 12, 3, 14, 7]
hasil = hitung_rata_rata(data)
print("Rata-rata dari data", data, "adalah", hasil)
# soal 3

    
# soal 4
def cari_nilai(a,b):
    if a == 0:
        return "nilai a tidak boleh 0"
    x = -b / a
    # kenapa bisa x = -b / a karena ax + b = 0, seperti pada soal
    return x
# print(cari_nilai(a,b))
# soal 7
def cek_gempa(data):
    if(data <= 2):
        print("mikro")
    elif(data >= 2 and data < 3):
        print("sangat lemah")
    elif(data >= 3 and data < 4):
        print("lemah")
    elif(data >= 4 and data < 5):
        print("ringan")
    elif(data >= 5 and data < 6):
        print("normal")
    elif(data >= 6 and data < 7):
        print("kuat")
    elif(data >= 7 and data < 8):
        print("utama")    
    elif(data >= 8):
        print("hebat")
# cek - cek_gempa(data)
# print(cek)
# soal 20
def tipe_segitiga(a,b,c):
    if a**2 + b**2 == c**2:
        return "segitiga siku-siku"
    elif a**2 + b**2 > c**2:
        return "segitiga lancip"
    else:
        return "segitga tumpul"
# print(tipe_segitiga(a,b,c))
# soal 21
def angka_ganjil(angka):
    ganjil = [angka for angka in angka if angka % 2 != 0]
    return ganjil

angka = [1,2,3,4,5,6,7,8,9]
hasil = angka_ganjil(angka)
print(hasil)

print("pilih fungsi yang ingin dijalankan")
print("1. mencari nilai a dan b")
print("2. cek data gempa")
print("3. cek jenis segitiga")

pilihan = int(input("masukan nomor fungsi yang akan dijalankan : "))
if pilihan == 1:
    a = int(input("masukan nilai a : "))
    b = int(input("masukan nilai b : "))
    cari_nilai(a,b)
elif pilihan == 2:
    data = float(input("masukan skala richter : "))
    cek_gempa(data)
elif(pilihan == 3):
    a = int(input("masukan nilai a : "))
    b = int(input("masukan nilai b : "))
    c = int(input("masukan nilai c : "))
    tipe_segitiga(a,b,c)
else:
    print("eror")