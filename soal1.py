# cara 1 
# data = [9,12,3,14,7]
# jumlah = sum(data)
# panjang = len(data) 
# # keterangan len = panjang array
# # mean = nilai rata-rata
# rata_rata = jumlah / panjang
# print(rata_rata);


# cara 2, menggunakan library (mungkin sedikit di curigai pak agung)
import statistics
def hitung_rata_rata(data):
    rata_rata = statistics.mean(data)
    return rata_rata

data = [9, 12, 3, 14, 7]
hasil = hitung_rata_rata(data)
print("Rata-rata dari data", data, "adalah", hasil)