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
