# casting adalah merubah satu tipe data ke tipe data lainnya
# tipe data = int, float, string, bool

print("=========INTEGER==========")
data_int = 10
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("=========FLOAT==========")
data_float = 10.7
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("=========BOOLEAN==========")
data_bool = False
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_float, ", type = ", type(data_float))

print("=========STRING==========")
data_str = "10"
print("data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str) # data string harus angka
data_float = float(data_str) # data string harus angka atau desimal
data_bool = float(data_str)
print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))