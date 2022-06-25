# funksiyalar

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib ilib salim beradi"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# print(salom_ber("Hasan"))
# print(salom_ber("Eldor"))
# print(print.__doc__)

# def yosh_hisobla(tugilgan_yil,joriy_yil=2020):
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
#
# print(yosh_hisobla(1998,2022))

# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi familiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# def toliq_ism_yasa(ism,familiya,otasining_ismi = ''):
#     """To'liq ism qaytaruvchi familiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa("shuhrat", "eshquvvatov")
# talaba2 = toliq_ism_yasa("Eldor","Poyonov","Abrorovich")
# print(f"Darsga kelmagan kelgan talabalar: {talaba1} va {talaba2}")
#
# def avto_info(kompaniya, model, rangi, korobka, yili, narh = None):
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rangi,
#         'koropka' : korobka,
#         'yili' : yili,
#         'narh' : narh
#     }
#     return avto
#
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2022)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2020, 14000)
# avtolar = [avto1, avto2]
# # print(avtolar[0]["rangi"])
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max,qadam = 1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(11, 22, 4))

# def avto_info(kompaniya, model, rangi, korobka, yili, narh = None):
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rangi,
#         'koropka' : korobka,
#         'yili' : yili,
#         'narh' : narh
#     }
#     return avto
# print("Saytimizdagi avtolar ro'yxatini shaklantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi malumotlarni kiriting", end='')
#     kompaniya = input(" Ishlab chiqaruvchisi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Koropka: ")
#     yili = input("Ishlab chiqilgan yili: ")
#     narhi = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     # Yana avto qo'shish - qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no):")
#     if javob == "no":
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto['narh']
#     else:
#         narh = "Nomalaum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} koropka. Narhi: {narh}")
# print(avtolar)

# Uyga vazifa

# def malumotnoma(ism, familiya, yosh, t_yil, t_joy, tel_raqam = None, e_manzil = ''):
#     malumot = {}
#     malumot['ism'] = ism
#     malumot['familiya'] = familiya
#     malumot['yosh'] = yosh
#     malumot["tug'ulgan yili"] = t_yil
#     malumot["tug'ulgan joy"] = t_joy
#     malumot["telfon raqami"] = tel_raqam
#     malumot["elektiron pochtasi"] = e_manzil
#     return malumot
# # shaxs = malumotnoma("Shuhrat","Eshquvvatov", 18, 1998, "Toshbuloq",
# #                     909006927, "eshquvvatovshuhrat98@gmail.com")
# # print(shaxs)
#
# mijozlar = []
# print("Assalomu alaykum hurmatli mijoz malumotlaringizni kiritin: ")
# while True:
#     ism = input("Ismingizni kiriting: ").title()
#     familiya = input("familiyangizni kiriting: ").title()
#     yosh = int(input("Yoshingizni kiriting: "))
#     t_yil = int(input("tug'ilgan yilingizni kiriting: "))
#     t_joy = input("tug'ilgan joyingizni kiriting: ").title()
#     tel_raqam = int(input("Telfon raqaminigizni kiriting: "))
#     elek_manzil = input("elektiron manzilingizni kiriting: ")
#     mijoz = malumotnoma(ism,familiya,yosh,t_yil,t_joy,tel_raqam,elek_manzil)
#     mijozlar.append(mijoz)
#     takror = input("Yana boshqa mijoz malumotlarini qo'shasizmi (ha/yo'q)?")
#     if takror == "yo'q":
#         break
# print(mijozlar)

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar
#
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# O'zgaruvchan funksiyalar
# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang = "Qora", yili = 2022)
# avto2 = avto_info("BMV", "X6", rang = "Qora", yili = 2022, narh = 35000, koropka = "avtomat")
# print(avto1)
# print(avto2)

# def talabalar(ism, familiya, **malumotlar):
#     malumotlar["ism"] = ism
#     malumotlar["familiya"] = familiya
#     return malumotlar
#
# talaba1 = talabalar("Jalil", "Jalilov", t_yil = 1999, yoshi = 23, buyi = 1.75, vazn = 80)
# print(talaba1)





























