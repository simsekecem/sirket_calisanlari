from Calisan import Calisan

class MaviYaka(Calisan):
    # Ozellikleri tanimla
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
        self.__yeni_maas = 0

    def get_yipranma_payi(self): # Veri okuma icin get metodu
        return self.__yipranma_payi

    def get_yeni_maas(self): # Veri okuma icin get metodu
        return self.__yeni_maas

    def set_yipranma_payi(self, yipranma_payi): # Deger atayabilmek icin set metodu
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self): # Zam ve yeni maasi hesaplama
        try:
            if self.get_tecrube() < 2:
                zam = (self.__yipranma_payi * 10)
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                zam = ((self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10))
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                zam = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
                self.__yeni_maas = self.get_maas() + (self.get_maas() * zam / 100)
            else:
                self.__yeni_maas = self.get_maas()
            return self.__yeni_maas
        except:
            return 0  # Hata durumunda programin cokmesini onlemek icin retun 0 kullanildi

    def __str__(self): # Ekrana yazdirmak icin str metodu
        try:
            self.zam_hakki()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.__yeni_maas}"
        except Exception as hata:
            print("Hata: ", hata)