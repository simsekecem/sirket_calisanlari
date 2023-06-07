from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

# Insan sinifindan nesneler olusturma
insan1 = Insan("123456789", "Ahmet", "Yılmaz", 25, "Erkek", "Türk")
insan2 = Insan("987654321", "Ayşe", "Demir", 30, "Kadın", "Türk")
insan3 = Insan("456789123", "Mehmet", "Öztürk", 35, "Erkek", "Türk")

print(insan1)
print("")
print(insan2)
print("")
print(insan3)
print("-----------")

# Issiz sinifindan nesneler olusturma
issiz1 = Issiz("1234567890", "Ahmet", "Yılmaz", 30, "Erkek", "Türk",{"beyaz yaka": 5, "mavi yaka": 30, "yonetici": 2})
issiz2 = Issiz("9876543210", "Ayşe", "Demir", 25, "Kadın", "Türk",{"mavi yaka": 4, "yonetici": 1})
issiz3 = Issiz("5555555555", "Mehmet", "Kara", 35, "Erkek", "Türk",{"beyaz yaka": 10, "yonetici": 5})

# Nesneleri ekrana yazdırma
print(issiz1)
print("")
print(issiz2)
print("")
print(issiz3)
print("...........")

# Calisan sinifindan nesneler olusturma
calisan1 = Calisan("12345678901", "Ahmet", "Yılmaz", 30, "Erkek", "Türk", "IT", 3, 12000)
calisan2 = Calisan("98765432109", "Ayşe", "Kara", 28, "Kadın", "Türk", "Muhasebe", 5, 20000)
calisan3 = Calisan("45678901234", "Mehmet", "Demir", 35, "Erkek", "Türk", "Üretim", 2, 10000)

# Nesneleri ekrana yazdırma
print(calisan1)
print("")
print(calisan2)
print("")
print(calisan3)
print("____________")
# MaviYaka sinifindan nesneler olusturma
mavi_yaka1 = MaviYaka("12345678901", "Ali", "Kaya", 30, "Erkek", "Türk", "Üretim", 20, 12000, 500)
mavi_yaka2 = MaviYaka("98765432109", "Ayşe", "Yılmaz", 28, "Kadın", "Türk", "Lojistik", 5, 18000, 700)
mavi_yaka3 = MaviYaka("45678901234", "Mehmet", "Demir", 35, "Erkek", "Türk", "Satış", 2, 10000, 400.8)

# Nesneleri ekrana yazdırma
print(mavi_yaka1)
print("")
print(mavi_yaka2)
print("")
print(mavi_yaka3)
print("**************")

# BeyazYaka sinifindan nesneler olusturma
beyaz_yaka1 = BeyazYaka("12345678901", "Ali", "Kaya", 30, "Erkek", "Türk", "Finans", 50, 20000, 1000)
beyaz_yaka2 = BeyazYaka("98765432109", "Ayşe", "Yılmaz", 28, "Kadın", "Türk", "İnsan Kaynakları", 5, 25000, 1500)
beyaz_yaka3 = BeyazYaka("45678901234", "Mehmet", "Demir", 35, "Erkek", "Türk", "Pazarlama", 2, 15000, 800)

# Nesneleri ekrana yazdırma
print(beyaz_yaka1)
print("")
print(beyaz_yaka2)
print("")
print(beyaz_yaka3)
print(".............")

# Aylari yillara cevirecek fonksiyon
def yil_cevir(ay):
    return f"{ay // 12} yil {ay % 12} ay"

# Database'i ekrana duzgun yazdirmak icin ayar
pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',13)

# Verilerle sozluk olusturma
data = {
    'Statu': ['çalışan', 'çalışan', 'çalışan', 'mavi yaka', 'mavi yaka', 'mavi yaka', 'beyaz yaka', 'beyaz yaka', 'beyaz yaka'],
    'tc_no': [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    'ad': [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    'soyad': [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    'yas': [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    'cinsiyet': [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    'uyruk': [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    'sektor': [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    'tecrube (yil)': [yil_cevir(calisan1.get_tecrube()), yil_cevir(calisan2.get_tecrube()), yil_cevir(calisan3.get_tecrube()), yil_cevir(mavi_yaka1.get_tecrube()), yil_cevir(mavi_yaka2.get_tecrube()), yil_cevir(mavi_yaka3.get_tecrube()), yil_cevir(beyaz_yaka1.get_tecrube()), yil_cevir(beyaz_yaka2.get_tecrube()), yil_cevir(beyaz_yaka3.get_tecrube())],
    'maas': [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    'yipranma_payi': [None, None, None, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), None, None, None],
    'tesvik primi': [None, None, None, None, None, None, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    'yeni maas': [None, None, None, mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas()]
}

# Sozluk ile database olusturma
df = pd.DataFrame(data)