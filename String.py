data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda /

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\Users\\Windows\\Reval")

# tab
print("Reval\t\tFahmi")

# backspace
print("Reval\bFahmi")

# newline
print("baris pertama.\nbaris kedua.") # LF -> Line Feed -> Biasanya digunakan pada unix, mac os, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> Biasanya digunakan pada OS Lama seperti Commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> List Feed Carriage Return -> Biasanya digunakan oleh Windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah path nya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama    : Reval Fahmi
Kelas   : 12 IPA 4
""")

# multiline literal string dan raw
print(r"""
Nama    : Reval Fahmi
Kelas   : 12 IPA 4 / New Normal
Website : https:\\kiwkiwkiw.com
""")