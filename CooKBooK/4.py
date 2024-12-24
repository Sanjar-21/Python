from collections import defaultdict # defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)
print(type(d))

a = defaultdict(set)
a['a'].add(1)
a['a'].add(2)
a['b'].add(4)
print(a['a'])
print(type(a))

a = {} # setdefault
a.setdefault('a', []).append(1)
a.setdefault('a', []).append(2)
a.setdefault('a', []).append(3)
a.setdefault('b', []).append(4)
a.setdefault('b', []).append(5)

print(a['a'])