import statistics 
# cara mengurutkan dari yang terkecil atau ascending
print("masukan pilihan")
print("1. secara asc")
print("2. secara desc")
pilihan = int(input("pilih asc atau desc : "))
if pilihan == 1:
    data = [9,12,3,14,7]
    data.sort()
    print(data)
elif pilihan == 2:
# cara mengurutkan dari yang terbesar atau descending
    data = [9,12,3,14,7]
    data.sort(reverse=True)
    print(data)
else:
    print("tidak valid")