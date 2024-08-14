

a = 10
b = 3

# operasi +
hasil = a + b
print(a,"+", b, "=", hasil)

# operasi -
hasil = a - b
print(a,"-", b, "=", hasil)

# operasi *
hasil = a * b
print(a,"*", b, "=", hasil)

# operasi /
hasil = a / b
print(a,"/", b, "=", hasil)

# operasi eksponen (pangkat)
hasil = a ** b
print(a,"**", b, "=", hasil)

# operasi modulus (%)
hasil = a % b
print(a,"%", b, "=", hasil)

# operasi floor division (//)
hasil = a // b
print(a,"//", b, "=", hasil)

# prioritas operasi, operational precedence

'''
    1. ()
    2. Eksponen
    3. Perkalian dan teman-teman
    4. Pertambahan dan pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)
