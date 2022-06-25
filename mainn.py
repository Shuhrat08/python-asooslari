
#modullarni import qilish
# 1- usul

# import avto_info_mod
#
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# avto_info_mod.info_print(avto1)

# import avto_info_mod as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# aim.info_print(avto1)


# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# iprint(avto1)

# from avto_info_mod import *
#
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)
#
#import random as r
# son = r.randint(0,100)
# print(son)

# ismlar = ["Anvar", "Olim", "Eldor", "Bobir"]
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# sonlar = list(range(0,50,5))
# print(sonlar)
# print(r.choice(sonlar))

# sonlar = list(range(0,50,5))
# print(sonlar)
# r.shuffle(sonlar)
# print(sonlar)

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
# kvadrat = lambda x, y : x ** y
# print(kvadrat(3,4))

# def daraja(n):
#     return lambda x : x ** n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(3))
# print(kub(3))

# from math import sqrt
#
# sonlar = list(range(0,11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# sonlar = list(range(0,11))
#
# def daraja2(x):
#     return x*x
#
# print(list(map(daraja2,sonlar)))

# sonlar = list(range(0,11))
#
# kvadrat = list(map(lambda x : x*x , sonlar))
# print(kvadrat)

# a = [4, 5, 6]
# b = [6, 7, 8]
# a_plus_b = list(map(lambda x,y : x + y, a,b))
# print(a_plus_b)

# import random as r
# sonlar = r.sample(range(100), 10)
# print(sonlar)
#
# def juftmi(x):
#     return x % 2 == 0
# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda son : son % 2 == 0,sonlar))
# print(juft_sonlar)

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", 'banan']
# harf = 'a'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))

#print(mevalar_b)

# mevalar2 = list(filter(lambda meva : len(meva) <= 5, mevalar))
# print(mevalar2)

mevalar_b = list(filter(lambda meva:meva.startswith('a') and meva.endswith('r'),mevalar))
print(mevalar_b)




