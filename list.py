import sys
# # 13.12.2024 # #
# # bugingi dars list # #
# # list belgisi [ ] ichiga yoziladi # #
mevalar = ['olam', 'gilos', 'anjir', 'hurmo'] 
print("mevelar size: " , sys.getsizeof(mevalar))
print(hex(id(mevalar)), "hotiradigi manzili") # hotiradan manzili
print(mevalar[0])
print(mevalar[1])
print(mevalar[2])
print(mevalar[3])
print(mevalar)
# # katta hariflar bilan chiqarib beradi # #
print(mevalar[0].upper()) 
print(mevalar[1].title())
print(mevalar[2].lower())
print(mevalar[3].capitalize())

# # Ruyhatga ohirga qushish
mevalar.append("olcha")
print(f"{mevalar}")
mevalar.insert(3, 'qovun')
mevalar.insert(2, " ")

# # list index orqali uchuirb yuborish

del mevalar[0]
meva = mevalar.pop(1)
print(f"{mevalar}")

"""

append ruyatni ohirdan qushish
insert ruyatni index orqali qushish
del uchrish index orqali
remove elemen orqali uchirish
pop listdan sug'rib olish

"""