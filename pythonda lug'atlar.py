'''car = {
    "model" : "Ferrari",
    "Rang" : "Qizil"
}
print(car["model"])
print(car["Rang"])
print(car)
'''
talaba_0 = {
    "ism" : "shuhrat eshquvvatov",
    "yosh" : 24,
    "t_yil" : 1998
}
'''print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tug'ilgan,\
 {talaba_0['yosh']} yoshda")
'''
talaba_0['kurs'] = 4
talaba_0['fakultet'] = "Informatika"
talaba_0['ism'] = "Elmurod"
print(talaba_0)
del talaba_0['fakultet']
print(talaba_0)
talaba = talaba_0.get('yunalish',"Bunday malumot mavjud emas")
print(talaba)