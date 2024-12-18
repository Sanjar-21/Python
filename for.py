# for sikli

mehmonlar = ["hasan", "ali", "vali", "malik", "omon"]
for mehmon in mehmonlar:
    print(f"salom {mehmon}")

# sonlar ustida ham for kuramiz

sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} sonlarni kvadrati {son**2} ga teng")

nums = list(range(11))
nums_kvadrati = []
for num in nums:
    nums_kvadrati.append(num**2)

print(f"{nums_kvadrati}")

dustlar = []
print("Beshta eng yaqin dustigizni belgilag: ")
for son in range(5):
    dustlar.append(input(f"{son+1}-dustignizni kirtig ismini: "))

print(dustlar)
