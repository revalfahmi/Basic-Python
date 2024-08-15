# operasi logika atau boolean

# not, and, and, xor

# NOT
print("=====NOT=====")
a = True
c = not a
print('data a = ', a)
print("===========NOT")
print('data c = ', c)

# OR
print("\n=====OR=====")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND
print("\n=====AND=====")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

# XOR
print("\n=====XOR=====")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)