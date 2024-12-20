avtolar = ['lasiti', 'mecsa', 'jugile', 'bmd']
for avto in avtolar:
    if avto == 'bmd':
        print(avto.upper())
    else:
        print(avto.title())

ism = input("ismigzni kritig: ")
if ism.lower() != 'ali':
    print(f"uzir {ism}, biz alini kutyabmiz")
else:
    print(f"salom {ism}")


yosh = int(input("Yoshingizni kirtig: "))
if yosh <= 18:
    print(f"sizga mumkinmas")
else:
    print(f"salom hushkelibsiz")