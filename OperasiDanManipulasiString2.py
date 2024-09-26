# operator dalam bentuk methods

## merubah case dari string

### Merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

### Merubah semua ke lower case
kota = "KoTa SukAbUmI"
print("normal = " + kota)
kota = kota.lower()
print("lower = " + kota)

### Contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya adalah boolean
print(salam + " is lower = ", str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya adalah boolean
print(salam + " is upper = ", str(apakah_upper))

### Is Alpha --> untuk pengecekan semuanya huruf
alpha = "Halonamasayaudin"
apakah_alpha = alpha.isalpha()
print(alpha + " is alpha = " + str(apakah_alpha))

### Is Alnum --> untuk pengecekan huruf dan angka
pwd = "Test123"
apakah_alnum = pwd.isalnum()
print(pwd + " is alnum = " + str(apakah_alnum))

### Is Decimal --> untuk mengecek angka
angka = "123456"
apakah_decimal = angka.isdecimal()
print(angka + " is decimal = " + str(apakah_decimal))

### Is Space --> untuk mengecek spasi
spasi = "Harusnya aku"
apakah_space = spasi.isspace()
print(spasi + " is spasi = " + str(apakah_space))

### Is Title --> untuk mengecek Huruf Awal pada kalimat
title = "Abdi Orang Dieu"
apakah_title = title.istitle()
print(title + " is title = " + str(apakah_title))

### ngecek komponen startswith() dan endswith() -> cek kalimat awal dan akhir, ini akan menghasilkan boolean
cek_start = "Persib Bandung".startswith("Persib")
print("start = ", str(cek_start))

cek_end = "Persib Bandung".endswith("Persib")
print("end = ", str(cek_end))

### menggabungkan dan memisahkan string --> join() dan split()
pisah = ['aku','sedang','mandi']
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "aku,sedang,mandi"
print(gabungan.split(",")) #ini akan menghasilkan list

### alokasi karakter rjust(), ljust(), dan center()
kanan = "No 1".rjust(20)
print("'"+kanan+"'")

kiri = "No 1".ljust(20)
print("'"+kiri+"'")

tengah = "No 1".center(20, "=")
print("'"+tengah+"'")

# strip() -> menghilangkan suatu symbol atau karakter
tengah = tengah.strip("=")
print("'"+tengah+"'")