words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_count = Counter(words)
takrorlanuchi_suzlar = word_count.most_common(6) # 6 ta takrorlanuvchi sizlar

print(takrorlanuchi_suzlar)

for son in takrorlanuchi_suzlar: # fro orqali  chiqarish birma bir
    print(son)