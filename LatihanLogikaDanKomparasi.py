# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++3----------10++++++

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10: "))
# memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print("Kurang dari 3 =", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10 =", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)


# -----3+++++++++++10------
# kasus irisan
print("\n", 10*"=", "\n")
inputUser = float(input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10: "))

# memeriksa angka lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# memeriksa angka kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

isCorrect = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ", isCorrect)

# Latihan
"""
    Masukkan angka
    1. ------O+++++++5------8+++++++11------
    2. ++++++O-------5++++++8-------11+++++++
"""

print("\n==========LATIHAN TUGAS===========\n")
inputan = float(input("Masukkan angka tugas 1: "))

# rules 1
isLebihDari0 = inputan > 0
isKurangDari5 = inputan < 5
isLebihDari8 = inputan > 8
isKurangDari11 = inputan < 11

jawaban = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("Angka yang anda masukkan: ", jawaban)

inputan = float(input("Masukkan angka tugas 2: "))

# rules 2
isKurangDari0 = inputan < 0
isLebihDari5 = inputan > 5
isKurangDari8 = inputan < 8
isLebihDari11 = inputan > 11

jawaban2 = isLebihDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print("Angka yang anda masukkan: ", jawaban2)
