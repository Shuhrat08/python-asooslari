class Avto:
    """Avto degan klass yaratamiz"""
    def __init__(self,model,nomi,rang,koropka,narh):
        self.model = model
        self.nomi = nomi
        self.rang = rang
        self.koropka = koropka
        self.narh = narh
        self.kilometr = 0

    def car_model(self):
        """Avtomobil modelini qaytaradi"""
        return self.model

    def car_rang(self):
        return self.rang

    def car_koropka(self):
        return self.koropka

    def car_narh(self):
        return self.narh

    def update_km(self,bos_km):
        """Avtomobil yurgan km ni ko'rsatib beradi """
        self.kilometr = bos_km

    def avto_info(self):
        return f"model: {self.model} nomi: {self.nomi} rangi : {self.rang}" \
               f" koropkasi : {self.koropka} narhi: {self.narh}$ "


class Avtosalon:
    def __init__(self,salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = []

    def get_salonnomi(self):
        """Avto salon haqida malumot"""
        return self.salon_nomi

    def get_salonmanzili(self):
        """Avto salon manzili"""
        return self.manzili

    def avto_baza(self):
        return [avto.avto_info() for avto in self.sotuvdagi_avtomobillar]

    def add_avto(self,avto):
        self.sotuvdagi_avtomobillar.append(avto)


avtosalon1 = Avtosalon("Car24","Sebzor")

avto1 = Avto("GM","Malibu", "qora", "avtomat", 23000)
avto2 = Avto("BMW","X6", "qora", "avtomat", 50000)
avto3 = Avto("Toyota","Toyota1", "Oq", "Gibred", 40000)
avtosalon1.add_avto(avto1)
avtosalon1.add_avto(avto2)
avtosalon1.add_avto(avto3)
print(avtosalon1.avto_baza())