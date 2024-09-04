import random
print("Merhabalar güçlü bir şifre oluşturmak çok önemlidir")
print("Güçlü şifreler hesaplarınızın çalınma riskini azaltır")
print("O yüzden bizim progmamımızı kulanmanızı öneririz")
print("İstediğiniz uzunlukta güçlü şifreler oluşturarak hesaplarınızın korumasını arttırırız")
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Lütfen şifrenizin uzunluğunu giriniz"))
                     
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakterler)


print("Şifreniz: " , sifre)
