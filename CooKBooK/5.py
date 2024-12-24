from collections import OrderedDict
import json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# for key, value in d.items():
#     print(key, d[key])

b = OrderedDict()
b['foo'] = 1
b['bar'] = 2
b['spam'] = 3
b['grok'] = 4
result = json.dumps(b)
print(result)
b['bar'] = 42
print(result)
