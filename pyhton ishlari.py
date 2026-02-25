#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 13:09:48 2026

@author: Abdu
"""
mevalar = {'olma': 10000, 'nok': 50000 , 'tarvuz':15000}
#print(mevalar)
#print(f"Olma narxi {mevalar['olma']} so`m")
car = {'model': 'ferrari', 'rang': 'qizil'}
#print (car['model'])
#print (car['rang'])
#talaba = {'ism': 'abdurahim', 'yosh':22, 't_yil':2004}
#print(f"{talaba['ism'].title()},\
# {talaba['t_yil']}-yilda tug`ilgan,\
# {talaba['yosh']}yoshda")
#talaba['kurs'] = 1
#talaba['fakultet'] = 'asosiy business'
#print(talaba)
#talaba['ism'] = 'abdu'
#print(talaba)
#print (talaba)
#print(talaba.items())

#for key, value in talaba.items():
#    print(f"Key: {key}")
#    print(f"Value: {value}\n")
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'nok':25000,
    'uzum':15000
    }
#print('Do`kondagi mahsulotlar:')
#for mahsulot in sorted (mahsulotlar):
#  print(mahsulot.title())
#bozorlik = ('o`rik', 'shaftoli', 'nok', 'olma')
#for mahsulot in mahsulotlar:
# if mahsulot in bozorlik:
  #print(f"{mahsulot.title()} {mahs"ulotlar[mahsulot]} so`m")
 
#for buyum in bozorlik:
  #  if buyum not in mahsulotlar:
      #  print(f"Iltimos, do`koningizga {buyum} ham olib keling!")
#print (mahsulotlar.values())
#print ('Foydalanuvchilar quyidagi narxlarda mevani olishadi:')
#for narx in mahsulotlar.values():
#    print(narx)

car0 = {
        'model': 'lacetti' ,
        'rang': 'qora' ,
        'yili': 2015 ,
        'narx': 12000 ,
        'karobka':'avtomat'
        }
car1 = {
        'model': 'nexia 3' ,
        'rang': 'qizil' ,
        'yili': 2010 ,
        'narx': 11000 ,
        'karobka': 'mexanika'
        }
car2 = {
        'model': 'gentra' ,
        'rang': 'oq' ,
        'yili': 2010 ,
        'narx': 12000 ,
        'karobka': 'avtomat'
        }
car = car2
#print (f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yili']}-yil, {car['narx']}$")

cars = [car0, car1,car2]
#for car in cars:#
#  print (f"{car['model'].title()}, "
#         f"{car['rang']} rang, "
#         f"{car['yili']}-yil, {car['narx']}$")    
#print (f"{cars[2] ['rang'].title()} "
#       f"{cars[2] ['model']}")

malibus=[]
for n in range(10):
    new_car = {
        "model": 'malibu' ,
        'rang': None, 
        'yil': 2020 ,
        'narx': None ,
        'km': 0 ,
        'karobka': 'avto'
        }
    malibus.append(new_car)
print(malibus)
for malibu in malibus:
    print(malibu)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus:
    print(malibu)
for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['karobka']='mexanika'
for malibu in malibus:
     print(malibu)  
for malibu in malibus:
    if malibu['karobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35500
for malibu in malibus:
    #print(malibu)
# %%

 dasturchilar = {
    'ali':['python' , 'c++'],
    'vali':['html' , 'css'],
    'jasur':['php' , 'python'],
    'xoshim':['phtyon' , 'c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarni biladi!")
    for til in tillar:
     print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi!")
    for til in tillar:
       print(f'{til.upper()} ' , end='')
# %%

ism = input('Ismingiz nima?\n>>>')
savol = f'Salom, {ism.title()}. Yoshingiz nechida?\n>>>'
yosh = input(savol)
yosh = int(yosh)
height = input ("Bo`yingiz necha metr?\n>>> ")
height = float(height)
# %%
#son = 1
#while son<=5:
#    print(son, end=' ')
#    son = son + 1 
#print('Dars tugadi')

#savol = "Istalgan sonni kiriting!"
#savol += "(dasturni to`xtatish uchun 'exit' deb yozing!):\n>>> "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#print('Dastur tugatildi!')

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 6:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng! ")


son = 0 
while son<10:
    son += 1
    if son%2==0:
     continue
    else:
     print(son)
# %%
     
print("Yaqin do`stlaringizni ro`yxatini tuzamiz!")
ismlar = []
n = 1 
while True:
    savol = f"{n}-do`stingizni kiriting:\n>"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo`shasizmi? (ha/yo`q)\n>")
    n+=1 
    if takrorlash != 'ha':
        break
     
print("Yaqin do`stlaringiz ro`yxati:")
for ism in ismlar:
    print(ism.title())
# %%
    
print("Do`stlaringizni yoshini saqlaymiz!")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do`stingizni ismini kiriting:\n>")
    yosh = input(f"{ism.title()}ning yoshini kiriting:\n>")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana malumot qo`shasizmi? (ha/yo`q)\n>")
    if javob == "yo`q":
        ishora = False
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
     
# %%

cars = ['lacetti', 'matiz', 'nexia', 'lacetti', 'matiz', 'nexia']
car = 'nexia'
while car in cars:
    cars.remove(car)
print (cars)
# %%

talabalar = ['hasan', 'ali', 'abdurahim', 'suxrob']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting!\n>")
    print(f"{talaba.title()} bahonlandi!")
    baholangan_talabalar[talaba] = int(baho)

# %%
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alekum")
salom_ber()
# %%

def salom_ber(ism):
    """Foydalanuvchining ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu alekum, hurmatli {ism.title()}!")
salom_ber('abdurahim')
# %%

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchining yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2026-tugilgan_yil} yoshda")
yosh_hisobla('abdurahim', 2004)
yosh_hisobla('xojiakbar', 2003)
yosh_hisobla(tugilgan_yil= 2003, ism='xojiakbar')
      
      
      
      
     
        
     
        
     
        
     
        
     
        
     
        
     