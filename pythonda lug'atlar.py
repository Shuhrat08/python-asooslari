'''car = {
    "model" : "Ferrari",
    "Rang" : "Qizil"
}
print(car["model"])
print(car["Rang"])
print(car)

talaba_0 = {
    "ism" : "shuhrat eshquvvatov",
    "yosh" : 24,
    "t_yil" : 1998
}
  print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tug'ilgan,\
 {talaba_0['yosh']} yoshda")

talaba_0['kurs'] = 4
talaba_0['fakultet'] = "Informatika"
talaba_0['ism'] = "Elmurod"

del talaba_0['fakultet']
print(talaba_0)
talaba = talaba_0.get('yunalish',"Bunday malumot mavjud emas")
print(talaba)


# Lug'at davomi
talaba_0 = {
    "ism" : "Shuhrat",
    "familiya" : "Eshquvvatov",
    "yosh" : 2,
    "fakultet" : "Kampyuter Injiniring",
    "kurs" : 4
    }
# #print(talaba_0.items())
# for key,value in talaba_0.items():
#     print(f"kalit : {key}")
#     print(f"qiymat : {value}\n")

telifonlar = {
    "ali" : "iphone x",
    "vali" : "galaxy s9",
    "olim" : "mi 10 pro",
    "orif" : "nlkia 3310",
    "hamida" : "galaxy s9",
    "maryam" : "huawei p30",
    "tohir" : "iphone x",
    "anvar" : "iphone x"
    }

#for k,q in telifonlar.items():
#    print(f"{k.title()}ning telifoni {q}")

mahsulotlar = {
    "olma" : 10000,
    "anor" : 20000,
    "uzum" : 40000,
    "shaftoli" : 30000,
    "banan" : 15000
}
# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ["anor", "uzum","non", "baliq", "banan"]
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"iltimos do'koningizga {buyum} olib keling")

# print(mahsulotlar.keys())
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

print("Foydalanuvchilar quyidagi telifonlarni ishlatadilar: ")
# for tel in telifonlar.values():
#      print(tel)
# for tel in set(telifonlar.values()):
#     print(tel)
toys = {"bear", "car", "lamp", "ball" ,"bear", "car"}
print(toys)

'''








