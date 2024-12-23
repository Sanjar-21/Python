# # Lug'at bilan ishlaymiz ikkinchi dars
talaba = {"ism": "Sanjar", "familya": "Xolmuminov", "fakultet": "IT", "kurs": 4}

# print(f"talalar ruyati {talaba.items()}")
# .items() dic hamasini chiqardi
for kalit, qiymat in talaba.items():
    print(f"Kalit -->{kalit}\nQiymat -->{qiymat}")

telfonlar = {"ali": "iphone x", "vali": "Nokia", "omon": "Readmi", "sanjar": "Samsug"}

for k, v in telfonlar.items():
    print(f"{k.title()} {v}")

# .keys() dic kalitlarni chiqarish uchun
print(f"{telfonlar.keys()}")
# .values() dic qiymatlarni kursatadi?
print(f"{telfonlar.values()}")
# set malumot turi
man = {"bir", "bir", "iki", "ikki"}
print(man)  # bu faqat bitalik ruhatni chiqaradi
