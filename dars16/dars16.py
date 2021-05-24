#1

#python = {
#    'if':'agar',
#    'in':'ichida',
#    'for':'uchun',
#    'or':'yoki',
#    'and':'va'
#    }
#for k, q in sorted(python.items()):
#    print(f"{k.capitalize()} - {q.capitalize()}")
   


#2


#davlatlar = {
#    'ozbekiston':'toshkent',
#    'rossiya':'moskva',
#    'turkiya':'istanbul',
#    'singapur':'singapur',
#    'tojikiston':'dushanbe'
#    }

#print("Dunyo davlatlari:")
#for d in sorted(davlatlar.keys()):
#    print(f"{d.title()}")

    
#print("Shu davlatlarning poytahtlari:")
#for p in sorted(davlatlar.values()):
#    print(f"{p.title()}")



#foy = input("Istalgan davlatni kiriting: ")
#if foy in davlatlar:
#    print(f"\"{foy.title()}\" ning poytahti: \"{davlatlar[foy].title()}\"")
#else:
#    print(f"Bizning ro'yhatda \"{foy.title()}\" davlati yo'q")




menu = {'osh':15000,"sho'rva":10000,'manti':8000,'somsa':6000,'lavash':14000}
foydalanuvchi = []
for foy in range(3):
    foydalanuvchi.append(input(f"{foy+1}- taom: "))
if foydalanuvchi:
    for foy in foydalanuvchi:
        if foy in menu:
            print(f"\"{foy.title()}\" ning narhi: {menu[foy]} so'm")
        else:
            print(f"Kechirasiz bizda \"{foy}\" yo'q")
else:
    print("Ro'yhat bo'sh")















