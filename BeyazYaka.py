from Calisan import Calisan

class BeyazYaka(Calisan):
    # Ozellikleri tanimla
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__yeni_maas = 0

    def get_tesvik_primi(self): # Veri okuma icin get metodu
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi): # Deger atayabilmek icin set metodu
        self.__tesvik_primi = tesvik_primi

    def get_yeni_maas(self): # Veri okuma icin get metodu
        return self.__yeni_maas

    def zam_hakki(self): # Zam ve yeni maasi hesaplama
        try:
            if self.get_tecrube() < 2:
                zam = self.__tesvik_primi
                self.__yeni_maas = self.get_maas() + zam
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                zam= (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
                self.__yeni_maas = self.get_maas() + zam
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                zam= (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
                self.__yeni_maas = self.get_maas() + zam
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