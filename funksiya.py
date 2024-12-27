# # 27 12 2024 
# # Funksiyalar haqida urganamiz

def salom_ber():
    print("Assalomu alaykum")

def salom_ism(ism):
    """ bu fuksiya ism strig -> ism oladi va salom beradi"""
    print(f"Assalomu alaykum hurmatli {ism.title()}")


salom_ber()
print('-' * 35)
print('-' * 35)
salom_ism('sanjar')
salom_ism('jalollidin') # funksiya haqda bilmoqchi bulsagiz print(salom_ism.__doc__)
# # funksiyani boshlanishga horicha shular buladi mencha yana chuqurlashamiz funksiya buyich 