# # 27 12 2024
# # itemgetter() — Dictionary ichidan kerakli kalitni olish uchun ishlatiladi. Bir yoki bir nechta kalitlarni qabul qilishi mumkin.1

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))

print('-'* 44)
print('-'* 44)
print(rows_by_fname)

print('-'* 44)
print('-'* 44)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

print('-'* 44)
print('-'* 44)

rows_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
print(rows_by_lfname)

print('-'* 44)
print('-'* 44)
# # lambda orqali ham qisa buladi buni
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(f"shu lambda orqali chiqarish {rows_by_fname}")

print('-'* 44)
print('-'* 44)
rows_by_lfname = sorted(rows, key=lambda r: (r['fname'], r['lname']))
print(f"lambda orqali fname lname {rows_by_lfname}")

min_rows = min(rows, key=itemgetter('uid'))
print(min_rows)
print('-'* 44)
max_rows = max(rows, key=itemgetter('uid')) # lambda orqali ham qisa ham buladi 
# min_rows = min(rows, key=lambda r: r['uid']) ; print(min_rows)
print(max_rows)