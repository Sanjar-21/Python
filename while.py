# while loop 25 12 2024
ism = input("Ismigizni kirtig: ")
savol = f"Salom {ism.title()} yoshigzni krtig: "
yosh = input(savol)
yosh = int(yosh)
hegit = input(f"{ism.title()} buyigiz qancha: ")
hegit = float(hegit)

son = 1
while son <= 5:
    print(son, end=" ")
    son += 1
print("dastur tagadi")

print("Istalgan soni kvatratini hosiblovchi dastur\n")
savol = input("Son krtig: ")
savol += f"\n(dasturni tuhtashi uchun 'exit' krtig: )"
qiymat = ""
while qiymat != "exit":
    qiymat = input(savol)
    if qiymat != "exit":
        print(float(qiymat) ** 2)

print("Istalgan soni kvatratini hosiblovchi dastur\n")
savol = input("Son krtig: ")
savol += f"\n(dasturni tuhtashi uchun 'exit' krtig: )"
qiymat = True
while qiymat:
    man = input(savol)
    if man == "exit":
        qiymat = False
    else:
        print(int(man) ** 2)

print("Istalgan soni kvatratini hosiblovchi dastur\n")
savol = input("Son krtig: ")
savol += f"\n(dasturni tuhtashi uchun 'exit' krtig: )"
while True:
    qiymat = input(savol)
    if qiymat == "exit":
        break
    else:
        print(f"{qiymat**2}")
nums = list(range(1, 11))
for son in nums:
    if son == 5:
        break
    print(f"son {son} kvadrati {son**2} ga teng")

nums = list(range(1, 11))
for son in nums:
    if son == 5:
        continue
    print(f"son {son} kvadrati {son**2} ga teng")
print("Dastur tuagadi")
