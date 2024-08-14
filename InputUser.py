# data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data : ", data, ", bertipe = ", type(data))

# jika kita ingin mengambil int, maka
data_int = int(input("masukkan angka: "))
print("data : ", data_int, ", bertipe = ", type(data_int))

# jika kita ingin mengambil float, maka
data_float = float(input("masukkan angka float: "))
print("data : ", data_float, ", bertipe = ", type(data_float))

# jika kita ingin mengambil bool, maka
data_bool = bool(int(input("masukkan angka bool: "))) # harus di casting ke int lagi
print("data : ", data_bool, ", bertipe = ", type(data_bool))