def theorema_pythagoras(a,b,c):
     hasil = a**2 + b**2
     return hasil == c**2

a = float(input("masukan nilai a : "))
b = float(input("masukan nilai b : "))
c = float(input("masukan nilai c : "))

result = theorema_pythagoras(a,b,c)
print(result)