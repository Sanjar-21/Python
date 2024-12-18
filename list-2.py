print("Listlar bilan ishlaymiz")

mevalar = [
    'olma',
    'gilos',
    'urik',
    'shatoli1'
]
# # sorted bu ruyatga tegmasdan tartib lab chiqaradi listni 

print(sorted(mevalar))
# # ruyhatdan tegmasdan teskarisga chiqarish
print(sorted(mevalar, reverse=True)) 

## agar listni tatiblash uchun 
mevalar.sort()
print(f" mevalar {mevalar}")

mevalar.sort(reverse=True)

print(f" mevalar {mevalar}")
# #  range(funksiya) bu sonlar ruyhatni qaytaradi ?
sonlar = list(range(1,11)) # 11  gacha bulgan sonlarni ruyhatini beradi ?
print(sonlar)
# # range bilan toq sonlar buladi
toq = list(range(1,11,2))
print(f"toq sonalar {toq}")
# # just sonlarga ham shunday buladi
juft = list(range(0,10,2))
print(f"just sonlar {juft}")
katta = max(juft) # max mim sonlar
mayda = min(toq) # min sonlar 
print(f"\tmax {katta} \n\tmin {mayda}")
num = sum(sonlar); print(num)
print(sonlar[0:4])
