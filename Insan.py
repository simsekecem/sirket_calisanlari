
class Insan:
    # Ozellikleri tanimla
    def __init__(self,tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def get_ad(self): # Veri okuma icin get metodu
        return self.__ad

    def set_ad(self, ad): # Deger atayabilmek icin set metodu
        self.__ad = ad

    def get_soyad(self): # Veri okuma icin get metodu
        return self.__soyad

    def set_soyad(self, soyad): # Deger atayabilmek icin set metodu
        self.__soyad = soyad

    def get_tc_no(self): # Veri okuma icin get metodu
        return self.__tc_no

    def set_tc_no(self, tc_no): # Deger atayabilmek icin set metodu
        self.__tc_no = tc_no

    def get_yas(self): # Veri okuma icin get metodu
        return self.__yas

    def set_yas(self, yas): # Deger atayabilmek icin set metodu
        self.__yas = yas

    def get_cinsiyet(self): # Veri okuma icin get metodu
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet): # Deger atayabilmek icin set metodu
        self.__cinsiyet = cinsiyet

    def get_uyruk(self): # Veri okuma icin get metodu
        return self.__uyruk

    def set_uyruk(self, uyruk): # Deger atayabilmek icin set metodu
        self.__uyruk = uyruk

    def __str__(self): # Ekrana yazdirmak icin str metodu
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"
