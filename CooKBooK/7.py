# # 25 12 2024
a = {"x": 1, "y": 2, "z": 3}  # 1  # 1 @  # 0

b = {"w": 10, "x": 11, "y": 2}  # 0  # 1  # 1 @

# bu yerda ikka lug'atni bir xillarni tekshiramiz .keys() kalitlarni tekshiradi
# print(a.keys() & b.keys()) # 1
# endi ularda
print(a.keys() - b.keys())  # a lug'atda lekin b da yuqini  kursatadi Z 0
print(b.keys() - a.keys())  # b lug'atda lekin a yuqini kursatadi W 0
# endi qiymat juftlarni aniqlaymiz
print(a.items() & b.items())  # ikkilasida qiymat bir hil @

# agar vayusi orqali amal bajaradigan bulas unda zip() foydalangan yahshi
print(set(a.values()) & set(b.values()))  # @
