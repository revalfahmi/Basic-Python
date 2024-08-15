# Program konversi celcius ke satuan lain

# print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input("Masukkan suhu dalam celcius: "))
# print("Suhu adalah = ", celcius, "Celcius")

# # Fahrenheit
# fahrenheit = ((9/5) * celcius) + 32
# print("Suhu dalam fahrenheit yaitu ", fahrenheit, "Fahrenheit")

# # Reamur
# reamur = (4/5) * celcius
# print("Suhu dalam reamur yaitu ", reamur, "Reamur")

# # Kelvin
# kelvin = celcius + 273
# print("Suhu dalam kelvin yaitu ", kelvin, "Kelvin")


## TASK KONVERSI FAHRENHEIT KE KELVIN DAN TASK KONVERSI KELVIN KE FAHRENHEIT

# Program konversi fahrenheit ke satuan lain

fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("Suhu adalah = ", fahrenheit, "Fahrenheit")

# celcius
celcius = ((fahrenheit - 32) * 5) / 9
print("Suhu dalam celcius yaitu ", celcius, "Celcius")

# kelvin
kelvin = ((fahrenheit - 459.67) * 5) / 9
print("Suhu dalam kelvin yaitu ", kelvin, "Kelvin")

# Program konversi kelvin ke satuan lain

kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("Suhu adalah = ", kelvin, "Kelvin")

#celcius
celcius = kelvin - 273
print("Suhu dalam celcius yaitu ", celcius, "Celcius")

#fahrenheit
fahrenheit = (kelvin * (9/5)) - 459.67
print("Suhu dalam fahrenheit yaitu ", fahrenheit, "Fahrenheit")

#reamur
reamur = (4/5) * (kelvin - 273)
print("Suhu dalam reamur yaitu ", reamur, "Reamur")