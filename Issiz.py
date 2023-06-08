from Insan import Insan

class Issiz(Insan):
    # Ozellikleri tanimla
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler
        self.__en_uygun_statu = None

    def get_tecrubeler(self): # Veri okuma icin get metodu
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler): # Deger atayabilmek icin set metodu
        self.__tecrubeler = tecrubeler

    def statu_bul(self): # En uygun statuyu hesaplama
        try:
            mavi_yaka_etkisi = 0.2
            beyaz_yaka_etkisi = 0.35
            yonetici_etkisi = 0.45
            max_etki = -100

            for statu, yil in self.get_tecrubeler().items():
                etki = 0
                if statu == "mavi yaka":
                    etki = yil * mavi_yaka_etkisi
                elif statu == "beyaz yaka":
                    etki = yil * beyaz_yaka_etkisi
                elif statu == "yonetici":
                    etki = yil * yonetici_etkisi

                if etki > max_etki:
                    max_etki = etki
                    self.__en_uygun_statu = statu

            return self.__en_uygun_statu

        except Exception as hata1:
            print("Hata: ", hata1)

    def __str__(self): # Ekrana yazdirmak icin str metodu
        try:
            self.statu_bul()
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nKişiye en uygun statü: {self.__en_uygun_statu}"
        except Exception as hata2:
            print("Hata: ", hata2)
