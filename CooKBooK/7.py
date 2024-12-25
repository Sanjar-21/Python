# # 25 12 2024
a = {
    'x': 1, # 1
    'y':2, # 1 @
    'z':3 # 0
}

b = {
    'w':10, # 0
    'x':11, # 1
    'y':2 # 1 @
}

# bu yerda ikka lug'atni bir xillarni tekshiramiz .keys() kalitlarni tekshiradi
# print(a.keys() & b.keys()) # 1
# endi ularda 
print(a.keys() - b.keys()) # a lug'atda lekin b da yuqini  kursatadi Z 0
print(b.keys() - a.keys()) # b lug'atda lekin a yuqini kursatadi W 0
# endi qiymat juftlarni aniqlaymiz
print(a.items() & b.items()) # ikkilasida qiymat bir hil @

# agar vayusi orqali amal bajaradigan bulas unda zip() foydalangan yahshi
print(set(a.values()) & set(b.values())) # @