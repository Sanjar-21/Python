# elif pythonda
son = int(input(f"son krtig: "))
if son <= 4:
    narh = 0
elif son <= 12:
    narh = 5
elif son <= 25:
    narh = 8
elif son <= 35:
    narh = 10
else:
    narh = 15
print(f"\tSizga narh {narh} so'm\n")

kun = input("kuni krtig: ")
if kun.lower() == "shanba" or kun.lower() == "yakshanba":
    print("Bugin kun dam olish kuni\n")
else:
    print("Bugin ish kuni\n")
