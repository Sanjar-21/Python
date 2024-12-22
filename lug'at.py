# # Pyrhonda Lug'at
# # 22 12 2024

book = {"nomi": "python", "rangi": "sariq", "qalinligi": 1000}

# print(f"kiton {book['nomi']}, rangi {book['rangi']}, qalinligi {book['qalinligi']}")

talaba = {"ism": "sanjar", "yosh": 20, "yil": 2004}
print(
    f"Talaba ismi {talaba['ism'].title()},\
      talaba yosh-{talaba['yosh']},\
      tug'ilgan yili-{talaba['yil']}"
)
# # Lug'atga malumot kirtish
talaba["kurs"] = 4
print(talaba)

# # get metidi shu lug'atda bormi yuqmi tekshiradi
# #

bir = talaba.get("isma", "Bunday suz mavjud emas")
print(bir)