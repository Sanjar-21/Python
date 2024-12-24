# # Nesting
# # 24 12 2024

car0 = {
    "model": "lasite",
    "rang": "Oq",
    "yil": 2018,
    "narh": 13000,
    "km": 50000,
    "karobka": "avtomat",
}

car1 = {
    "model": "nexia-3",
    "rang": "Qora",
    "yil": 2015,
    "narh": 9000,
    "km": 30000,
    "karobka": "mexanika",
}

car2 = {
    "model": "shentra",
    "rang": "Qizil",
    "yil": 2016,
    "narh": 18000,
    "km": 10000,
    "karobka": "mexanika",
}

# car = car2
# print(f"{car['model'].title()} ",
#       f"{car['rang']}\n"
#       f"{car['yil']}")

# # oson yuli
cars = [car0, car1, car2]
# print(cars)
# print(type(cars))

for car in cars:
    print(f"{car['rang'].title()}, " f"{car['km']}", f"{car['yil']}")

print(cars[2]["rang"], "listdan chiqarish index orqali")

malubi = []  # bush list uni for bilan tuldiramiz
for n in range(11):
    new_car = {
        "model": "malubi",
        "rang": None,
        "yil": 2020,
        "narh": None,
        "km": 20000,
        "korobka": None,
    }
    malubi.append(new_car)
