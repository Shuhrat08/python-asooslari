# print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# sonning tup yoki murakkab ekanligini aniqlash
# n = int(input("son kiriting: "))
# k = 0
# i = 1
# while i <= n:
#     if n % i == 0:
#         k += 1
#     i += 1
# if k == 2:
#     print(n,"sini tup son")
# else:
#     print(n,"soni murakkab son")

# son = input("son kiriting: ")
# orin = int(input("qaysi o'rindagi son kerak sizga: "))
# print(son[-orin])

# print("Yaqin do'stlaringiz ismini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shmoqchimisiz? (ha/yo'q)")
#     n += 1
#     if takrorlash != 'ha':
#         break
# print("Sizning yaqin do'stlaringiz:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()} ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana malumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
# print(dostlar)

# cars = ['lasetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia', 'lasetti']
# car = 'nexia'
# while car in cars:
#     cars.remove(car)
#
# print(cars)

# talabalar = ['hasan', 'husan', 'eldor', 'elmurod']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(talabalar)
# print(baholangan_talabalar)

#foydalanuvchidan buyritma qabul qilamiz

buyurtma = []
taom = input("Assalomu alaykum siz nima buyrutma qilasiz: ")
while True:
    buyurtma.append(taom)
    taom = input(f"tugatish uchun ha yoki yo'q bising \n{taom.title()} yozdik yana nima buyrutma qilasiz: ")
    if taom == "yo'q":
        buyurtma.append(taom)
        break
print("Sizning buyrutmangiz", buyurtma)


