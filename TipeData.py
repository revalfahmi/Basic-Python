# tipe data: Angka satuan (integer)
data_integer = 1
print(type(data_integer))
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: Angka desimal atau ada koma nya (float)
data_float = 1.5
print(type(data_float))
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "Hello World"
print(type(data_string))
print("data : ", data_string, ", bertipe : ", type(data_string))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print(type(data_complex))
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe dari bahasa c
from ctypes import c_double

data_c_double = c_double(10.5)
print(type(data_c_double))
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))