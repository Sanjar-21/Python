print("Listlar bilan ishlaymiz")

mevalar = [
    'olma',
    'gilos',
    'urik',
    'shatoli1'
]
# # sorted bu ruyatga tegmasdan tartib lab chiqaradi listni 

print(sorted(mevalar, reverse=True))

## agar listni tatiblash uchun 
mevalar.sort()
print(f" mevalar {mevalar}")

mevalar.sort(reverse=True)

print(f" mevalar {mevalar}")