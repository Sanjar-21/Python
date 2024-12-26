# # ruyhatdan ikkita kegan sonlarni olib tashlash va bir hil qiymat qilib chiqarish 
# # 26, 12, 2024
def sartorofka(itmes):
    seen = set()
    for item in itmes:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(sartorofka(a))) # [1, 5, 2, 9, 10]
# Lug'at uchun 

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

# yield nima ekanligini tushunamiz
def simple_gen():
    yield 1
    yield 2
    yield 3
    yield 4

print(next(simple_gen()))

print('-'* 44)
print('-'* 44)

items = [1,2,2,1,3]
key = None

seen = set()
reault = []

for item in items:
    val = item if key is None else key(item)
    if val not in seen:
        reault.append(item)
        seen.add(item)

print(reault)
print(seen)
print('-'* 44)
print('-'* 44)

def son(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(son(items)))