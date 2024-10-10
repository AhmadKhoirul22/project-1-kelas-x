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
data = float(input("masukan skala richter : "))
cek_gempa(data)
