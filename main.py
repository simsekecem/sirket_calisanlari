from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

# Insan sinifindan nesneler olusturma
insan1 = Insan("1234564805", "Harun", "Çalışkan", 25, "Erkek", "Türk")
insan2 = Insan("9876536926", "Yıldız", "Tahinoğlu", 30, "Kadın", "Türk")
insan3 = Insan("4567839063", "Tarık", "Öztürk", 35, "Erkek", "Türk")

print(insan1)
print("")
print(insan2)
print("")
print(insan3)
print("-----------")

# Issiz sinifindan nesneler olusturma
issiz1 = Issiz("1234567890", "Sadullah", "Ak", 30, "Erkek", "Türk",{"beyaz yaka": 5, "mavi yaka": 30, "yonetici": 2})
issiz2 = Issiz("9876543210", "Rümeysa", "Yalçın", 25, "Kadın", "Türk",{"mavi yaka": 4, "yonetici": 1})
issiz3 = Issiz("5555555555", "Selen", "Kara", 35, "Erkek", "Türk",{"beyaz yaka": 10, "yonetici": 5})

# Nesneleri ekrana yazdırma
print(issiz1)
print("")
print(issiz2)
print("")
print(issiz3)
print("...........")

# Calisan sinifindan nesneler olusturma
calisan1 = Calisan("37024678901", "Ahmet", "Yılmaz", 30, "Erkek", "Türk", "IT", 7, 12000)
calisan2 = Calisan("56745432109", "Ayşe", "Kara", 28, "Kadın", "Türk", "Muhasebe", 5, 30000)
calisan3 = Calisan("17498901234", "Mehmet", "Demir", 35, "Erkek", "Türk", "Üretim", 9, 10000)

# Nesneleri ekrana yazdırma
print(calisan1)
print("")
print(calisan2)
print("")
print(calisan3)
print("____________")

# MaviYaka sinifindan nesneler olusturma
mavi_yaka1 = MaviYaka("12345678901", "Ali", "Kaya", 30, "Erkek", "Türk", "Üretim", 20, 12000, 0.2)
mavi_yaka2 = MaviYaka("98765432109", "Güneş", "Yılmaz", 28, "Kadın", "Türk", "Lojistik", 5, 18000, 0.3)
mavi_yaka3 = MaviYaka("45678901234", "Kerim", "Gök", 35, "Erkek", "Türk", "Satış", 2, 10000, 0.4)

# Nesneleri ekrana yazdırma
print(mavi_yaka1)
print("")
print(mavi_yaka2)
print("")
print(mavi_yaka3)
print("**************")

# BeyazYaka sinifindan nesneler olusturma
beyaz_yaka1 = BeyazYaka("74075678901", "Salih", "Mehmet", 30, "Erkek", "Türk", "Finans", 50, 20000, 1000)
beyaz_yaka2 = BeyazYaka("98765458370", "Hande", "Yılmaz", 28, "Kadın", "Türk", "İnsan Kaynakları", 5, 25000, 1500)
beyaz_yaka3 = BeyazYaka("45678906359", "Selim", "Güven", 35, "Erkek", "Türk", "Pazarlama", 2, 15000, 800)

# Nesneleri ekrana yazdırma
print(beyaz_yaka1)
print("")
print(beyaz_yaka2)
print("")
print(beyaz_yaka3)
print(".............")

# Aylari yillara cevirecek fonksiyon
def yil_cevir(ay):
    yil = ay/12
    yil = round(yil, 2)
    return yil

# Dataframe'i ekrana duzgun yazdirmak icin ayar
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
    'yeni maas': [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(), mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas()]
}

# Sozluk ile dataframe olusturma
df = pd.DataFrame(data)

# Bos yerlere sifir atama
df = df.fillna(0)

# Dataframe'i ekrana yazdir
print(df)
print("")
print("")

# Yeni maasa gore sirala ve ekrana yazdir
print("Yeni maasa gore siralama:")
yeni_maas_df = df.sort_values('yeni maas')
print(yeni_maas_df)
print("")
print("")

# Maasi 15bin uzeri olan kisi sayisi
sayac=0
for maaslar in df['maas']:
    if maaslar >15000:
        sayac+=1
print(f"maasi 15000TL üzeri olan {sayac} kisi var")
print("")
print("")

# Calisan, mavi yaka ve beyaz yaka icin tecrube ve maas ortalamalari
gruplanmis_df = df.groupby('Statu').agg({'tecrube (yil)': 'mean', 'yeni maas': 'mean'})
print("Calisan, mavi yaka ve beyaz yakaların tecrube ve maas ortalamalari")
print(gruplanmis_df)
print("")
print("")

# Tecrubesi 3 yildan fazla olan beyaz yakalilar
beyaz_yakalar = df[(df['Statu'] == 'beyaz yaka') & (df['tecrube (yil)'] > 3)]
print("Tecrubesi 3 yildan fazla olan beyaz yakalilar: ")
print(beyaz_yakalar)
print("")
print("")

# Maasi on bin tl uzeri olanlar
onbinmaas = (df['yeni maas'] > 10000)
secilen_satirlar = df[onbinmaas].iloc[2:6, [1, -1]]  # 2-5 satirları ve tc ve yeni maas sutunlari
print("Yeni maasi 10000 TL uzerinde olanlar icin 2-5 satir arasi olanlar, tc no ve yeni maas sutunlari")
print(secilen_satirlar)
print("")
print("")

# Ad, soyad, sektor, yeni maasi iceren yeni dataframe olusturma
print("Ad, soyad, sektor ve yeni maasi iceren yeni dataframe: ")
yeni_df = df[['ad', 'soyad', 'sektor', 'yeni maas']]
print(yeni_df)
