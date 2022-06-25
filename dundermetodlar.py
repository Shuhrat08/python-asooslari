from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self ,make ,model ,rang ,yil ,narh ,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"

    def __eq__(self, other):
        return self.narh ==other.narh

    def __lt__(self, other):
        return self.narh < other.narh

    def __le__(self, other):
        return self.narh <= other.narh

class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __getitem__(self, item):
        return self.avtolar[item]

    def __setitem__(self, key, value):
        self.avtolar[key] = value

    def __call__(self, *qiymat, **kwargs):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]

    def __add__(self, qiymat):
        if isinstance(qiymat,Avtosalon):
            yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avtolar qo'shing")


salon1 = Avtosalon("Maxavto")
salon2 = Avtosalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
# salon1[0] = Avto("BMW", "X7","Qora",2022,70000)
salon2(avto4,avto5,avto6)
# salon3 = salon1 + salon2
# salon3.name = "MaxLider Avto"
salon1 + avto4
print(salon1())