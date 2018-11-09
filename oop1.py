class Calisan:
    counter = 0
    zam_oran = 1.8
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.email = ad+soyad+"@hotmail.com"
        Calisan.counter += 1

    def nameSurnameYazdir(self):
        return self.ad+" "+self.soyad

    def zamYap(self):
        self.maas = self.maas + self.maas*self.zam_oran

calisan1 = Calisan("ali","veli",100)
calisan2 = Calisan("deli","alim",200)
calisan3 = Calisan("kerim","kemik",300)
calisan4 = Calisan("kezban","demir",400)

print(calisan1.nameSurnameYazdir())
calisan1.zamYap()
print("yeni maas : ",calisan1.maas," lira")

listee = [calisan1, calisan2, calisan3, calisan4]

maxmaas = -1
index = -1

for e in listee:
    if (e.maas > maxmaas):
        maxmaas = e.maas
        index = e
print()
print("en yüksek maaşı alan kişi : ", e.nameSurnameYazdir())
print(maxmaas," TL")

