import re
import os
from collections import defaultdict

os.system('cls' if os.name == 'nt' else 'clear')

banner = r"""
 _____ _   _      _            __  __      _   _        ___          _   _ 
|_   _(_) (_)_ __| | _____ ___|  \/  | ___| |_(_)_ __  / _ \ _______| |_(_)
  | | | | | | '__| |/ / __/ _ \ |\/| |/ _ \ __| | '_ \| | | |_  / _ \ __| |
  | | | |_| | |  |   < (_|  __/ |  | |  __/ |_| | | | | |_| |/ /  __/ |_| |
  |_|  \__,_|_|  |_|\_\___\___|_|  |_|\___|\__|_|_| |_|\___//___\___|\__|_|
                       )_)                                                 
"""
print(banner)

def kelime_frekansi_hesapla(metin):
    metin = re.sub(r'[^a-zA-ZçÇğĞıİöÖşŞüÜ\s]', '', metin.lower())
    kelimeler = metin.split()
    kelime_frekansi = defaultdict(int)
    for kelime in kelimeler:
        kelime_frekansi[kelime] += 1
    
    return kelime_frekansi

def cumle_skorla(metin, kelime_frekansi):
    cumleler = re.split(r'(?<=[.!?]) +', metin)
    
    cumle_skorlari = defaultdict(float)

    for cumle in cumleler:
        kelimeler = cumle.split()
        cumle_skoru = 0
        for kelime in kelimeler:
            cumle_skoru += kelime_frekansi.get(kelime.lower(), 0)
        cumle_skorlari[cumle] = cumle_skoru
    
    return cumleler, cumle_skorlari

def ozet_cikar(cumleler, cumle_skorlari, cumle_sayisi):
    en_iyi_cumleler = sorted(cumle_skorlari, key=cumle_skorlari.get, reverse=True)[:cumle_sayisi]
    
    ozet = [cumle for cumle in cumleler if cumle in en_iyi_cumleler]
    return ' '.join(ozet)

def metin_ozetle(metin, cumle_sayisi=3):
    kelime_frekansi = kelime_frekansi_hesapla(metin)
    cumleler, cumle_skorlari = cumle_skorla(metin, kelime_frekansi)
    ozet = ozet_cikar(cumleler, cumle_skorlari, cumle_sayisi)
    
    return ozet

metin = """Python, yüksek seviyeli, genel amaçlı bir programlama dilidir. 
Yazılımlar geliştirmek için kullanılır ve birçok alanda kullanımı yaygındır. 
Python'un kolay öğrenilebilir ve okunabilir olması popülerliğini artırmıştır. 
Ayrıca Python, yapay zeka, veri bilimi ve web geliştirme gibi alanlarda yaygın olarak kullanılmaktadır."""

ozet = metin_ozetle(metin, cumle_sayisi=2)
print("Metin:\n\n", metin, "\n\n\n", "Özet:\n", ozet)

