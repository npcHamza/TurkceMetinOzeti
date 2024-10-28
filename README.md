
# Türkçe Metin Özeti - Türkçe Metin Özetleme Aracı

Türkçe Metin Özeti, Türkçe metinleri özetlemek için kullanılan basit bir Python scriptidir. Kelime zinciri algoritması temel alınarak yazılmıştır. Bu araç, kullanıcıların uzun metinleri hızlıca özetlemelerine yardımcı olur.

## Özellikler
- Metin içerisindeki kelimelerin frekansını analiz eder.
- En yüksek skorlu cümleleri seçerek özet oluşturur.
- Terminal arayüzünde kullanıcı dostu bir banner görüntüler.

## Gereksinimler
Bu script, Python 3.x sürümünü gerektirir. Ek bir kütüphane kullanılmadığı için ek bir yükleme yapılmasına gerek yoktur.

## Kurulum
1. Python'un sisteminizde yüklü olduğundan emin olun.
2. Scripti bir `.py` dosyası olarak kaydedin (örneğin, `main.py`).

## Kullanım
Scripti çalıştırmak için terminal veya komut istemcisine gidin ve şu komutu kullanın:

```bash
python ozmetin.py
```

### Örnek
Script içinde bulunan örnek metin ile çalışacaktır. İsterseniz `metin` değişkeninin içeriğini kendi metninizle değiştirebilirsiniz.

## Nasıl Çalışır?
1. **Terminal Temizleme**: Script çalıştığında terminali temizler.
2. **Banner Yazdırma**: Kullanıcıya hoş bir karşılama banner'ı gösterir.
3. **Kelime Frekansı Hesaplama**: Metindeki kelimelerin frekansını hesaplar.
4. **Cümle Skorlama**: Cümleleri kelime frekanslarına göre puanlar.
5. **Özet Çıkarma**: En yüksek skorlu cümleleri bir araya getirerek özet oluşturur.
