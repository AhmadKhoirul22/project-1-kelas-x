def tipe_segitiga(a,b,c):
    if a**2 + b**2 == c**2:
        return "segitiga siku-siku"
    elif a**2 + b**2 > c**2:
        return "segitiga lancip"
    else:
        return "segitga tumpul"
a = int(input("masukan nilai a : "))
b = int(input("masukan nilai b : "))
c = int(input("masukan nilai c : "))

print(tipe_segitiga(a,b,c))
# 345 = segitiga sikusiku
# 346 = segitiga tumpul
# 51215 = segitiga lancip
# return tipe_segitiga(a,b,c)