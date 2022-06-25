
# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def get_name(self):
#         return self.ism
#
#     def get_age(self,yil):
#         return yil - self.tyil
#
#     def get_lastname(self):
#         return self.familiya
#
#
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya} tug'ilgan yilim {self.tyil}"
# talaba1 = Talaba("Shuhrat", "Eshquvvatov", 1998)
# talaba2 = Talaba("Elmurod", "Normurodov", 1998)
# talaba3 = Talaba("Ismoil", "Ergashaliyev", 1999)
# print(talaba1.ism)
# print(talaba3.tanishtir())

# class User:
#     def __init__(self,ism,familiya,foy_ismi,e_mail,):
#         self.ism = ism
#         self.familiya = familiya
#         self.foy_ismi = foy_ismi
#         self.e_mail = e_mail
#
#     def get_info(self):
#         return f"Foydalanuvchi {self.foy_ismi} ismi: {self.ism} {self.familiya} email: {self.e_mail}"
#
# user1 = User("Shuhrat", "Eshquvvatov", "shuhrat98","eshquvvatovshuhrat98@gmail.com")
# print(user1.get_info())


class Talaba:
    "Talaba nomli klass yaratamiz"
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def set_bosqich(self,yangi_bosqich):
        """Talabaning yangi bosqich o'tganini qaytaradi"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabaning bosqichini 1 kurs yuqoriga kutaradi"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida umumiy malumot"""
        return f"{self.ism} {self.familiya} {self.bosqich} - bosqich talabasi"

class Fan:
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def get_students(self):
        """Fanga yozilgan talabalar haqida malumot"""
        # talabalar = []
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_fullname())
        # return talabalar
        return [talaba.get_fullname() for talaba in self.talabalar]

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

matem = Fan("Oliy matematika")
talaba1 = Talaba("Shuhrat", "Eshquvvatov", 1998)
talaba2 = Talaba("Elmurod", "Normurodov", 1998)
talaba3 = Talaba("Ismoil", "Ergashaliyev", 1999)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
print(matem.get_students())
print(dir(Talaba))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(see_methods(talaba1))
print(talaba1.__dir__())
print(talaba1.__dict__.values())