# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari (>)
print("========== LEBIH BESAR DARI (>)")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# lebih kecil dari (<)
print("========== LEBIH KECIL DARI (<)")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih besar dari sama dengan (>=)
print("========== LEBIH BESAR DARI SAMA DENGAN (>=)")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# lebih kecil dari sama dengan (<=)
print("========== LEBIH KECIL DARI SAMA DENGAN (<=)")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan (==)
print("========== SAMA DENGAN (==)")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidak sama dengan (!=)
print("========== SAMA DENGAN (!=)")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi object identity
print("========== OBJECT IDENTITY (IS)")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

# 'is' sebagai komparasi object identity
print("========== OBJECT IDENTITY (IS NOT)")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y = ', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)