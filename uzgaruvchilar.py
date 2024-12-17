# 12.12.2024
# Python 3.12.7 versiyasi
# Python uzgaruvchilar c tilidan farqli uraloq
# hotiradan joy olmaydi tug'ridan tug'ri
# python da RAM joy oladi?
import sys

yosh = 20
number = 23242323232342423
ism = "Sanjar"
s = 21.21
print(f"Ism {ism} \n Yosh {yosh}")
# pythonda RAM da turgan joyi uzgaruvchilarni ?
print("Yoshni sizoefi", sys.getsizeof(yosh))
print("Ismni sizeofi", sys.getsizeof(ism))
print(" Number: ", sys.getsizeof(number))
print(sys.platform)  # sestime haqida habar beradi ?
print("Flaotni sizeof", sys.getsizeof(s))
print("Xotira manzili", hex(id(yosh)))
