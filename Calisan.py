from Insan import Insan

class Calisan(Insan):
    # Ozellikleri tanimla
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = 0

    def get_sektor(self): # Veri okuma icin get metodu
        return self.__sektor

    def set_sektor(self, sektor): # Deger atayabilmek icin set metodu
        self.__sektor = sektor

    def get_tecrube(self): # Veri okuma icin get metodu
        return self.__tecrube

    def set_tecrube(self, tecrube): # Deger atayabilmek icin set metodu
        self.__tecrube = tecrube

    def get_maas(self): # Veri okuma icin get metodu
        return self.__maas

    def set_maas(self, maas): # Deger atayabilmek icin set metodu
        self.__maas = maas

    def get_yeni_maas(self): # Veri okuma icin get metodu
        return self.__yeni_maas

    def zam_hakki(self): # Zam hakki ve maas hesaplama
        try:
            if self.__tecrube < 2:
                zam = 0
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                zam = ((self.__maas % self.__tecrube)  + self.__maas)
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            elif self.__tecrube > 4 and self.__maas < 25000:
                zam = (((self.__maas % self.__tecrube) / 2) + self.__maas)
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            else:
                self.__yeni_maas = self.get_maas()
            return self.__yeni_maas
        except:
            return 0 # Hata durumunda programin cokmesini onlemek icin retun 0 kullanildi

    def __str__(self): # Ekrana yazdirmak icin str metodu
        try:
            self.zam_hakki()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.__yeni_maas}"
        except Exception as hata:
            print("Hata: ", hata)
