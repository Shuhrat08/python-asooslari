

class Shaxs:
    """Shaxs haqida malumotlar"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida malumotlar"""
        info = f"{self.ism} {self.familiya}. Passport: {self.passport}," \
               f" {self.tyil}-yilda tug'igan"
        return info

    def get_age(self,yil):
        """Shaxs yoshini qaytaradi"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil


    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


class Mamzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rsatish"""
        manzil = f"{self.viloyat} viloyati {self.tuman} tumani, " \
                 f"{self.kocha} ko'chasi {self.uy} uy"
        return manzil


talaba_manzil = Mamzil(18,"Yangi Sebzor","Olmazor","Toshkent")
talaba1 = Talaba("Shuhrat","Eshquvvatov","AB1181343",1998,"N0001998",talaba_manzil)
print(talaba1.manzil.get_manzil())
# print(talaba1.get_id())
# print(talaba1.get_age(2022))
# print(talaba1.get_info())