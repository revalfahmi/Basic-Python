# operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Reval"
nama_tengah = "D"
nama_terakhir = "Aziz"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_terakhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string
r = "R"
status = r in nama_lengkap
print(r + " ada di " + nama_lengkap + " = " + str(status))

# mengecek apakah tidak ada komponen char atau string di string
d = "e"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10) #bisa didepan
print(15*"wk") #bisa dibelakang

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-(0-3) : " + nama_lengkap[0:4])
print("index ke-(3-7) : " + nama_lengkap[3:8])
print("index ke-(0-11) : " + nama_lengkap[0:12:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling kecil : " + max(nama_lengkap))

asciii_code = ord("R")
print("ASCII code untuk R adalah " + str(asciii_code))
data = 120
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "Reval Fahmi Aziz"
jumlah = data.count("a")
print("jumlah a pada " + data + " adalah = ", jumlah)