prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}
min_prices = min(zip(prices.values(), prices.keys()))
max_prices = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
prices_and_name = zip(
    prices.values(), prices.keys()
)  # zip qayta qayta ishlatish tavsiya qilinmaydi
# print(min_prices)
# print(max_prices)
# print(prices_sorted)
print(min(prices_and_name))
# print(max(prices_and_name))
# zip() iteratorni faqat bir marta ishlatadi: Agar zip() natijasi bir marta ishlatilgan bo‘lsa, u bo‘sh bo‘lib qoladi:
# Traceback (most recent call last):
#   File "/home/sanjar/Python/CooKBooK/6.py", line 16, in <module>
#     print(max(prices_and_name))
#           ^^^^^^^^^^^^^^^^^^^^
# ValueError: max() iterable argument is empty

print(min(prices))
print(max(prices))
min_key = min(prices, key=lambda k: prices[k])
max_key = max(prices, key=lambda k: prices[k])
print(f"min topish prices {min_key} \nmax topish prices {max_key}")
# valusini sal bashqacharoq topiladi
min_valu = prices[min(prices, key=lambda k: prices[k])]
max_valu = prices[max(prices, key=lambda k: prices[k])]
print(f"min valu {min_valu}\nmax valu {max_valu}")

# print(min(prices.values())) # bu yilar ham bor shularni ishlatishsa ham buladi
# print(max(prices.keys())) # bu yilar ham bor shularni ishlatishsa ham buladi
