
# Türkçe Metin Özetleyici
![Banner](https://raw.githubusercontent.com/npcHamza/TurkceMetinOzeti/refs/heads/main/banner.png)
Türkçe Metin Özetleyici, uzun Türkçe metinleri analiz ederek özet çıkarmaya yarayan bir Python scriptidir. Metin içerisindeki cümleleri frekansa dayalı puanlama yöntemiyle seçer ve özlü bir sonuç sunar. Bu script, terminal tabanlı bir arayüz ile kullanıcıya kolaylık sağlar.

## Özellikler
- Terminal üzerinden `.txt` dosyalarınızı seçmenize olanak tanır.
- Seçilen dosyaların içeriğini analiz eder ve belirli sayıda cümle ile özet oluşturur.
- Kullanıcıya dostu, renkli bir banner gösterir.
- Dosya önizlemeleri ve özetler tablolar halinde görüntülenir.
- Oluşturulan özeti kaydetme seçeneği sunar.

## Gereksinimler
- Python 3.x yüklü olmalıdır.
- Ek olarak, `colorama`, `rich` gibi kütüphanelerin yüklü olması gereklidir. Kütüphaneleri yüklemek için:
  ```bash
  pip install colorama rich
  ```

## Kurulum
1. `main.py` dosyasını bir klasöre kaydedin.
2. Terminalde bu klasöre gidin.

## Kullanım
Terminalde scripti çalıştırmak için:
```bash
python main.py
```

## Kullanım Adımları
1. Çalıştırdığınızda, mevcut dizindeki tüm `.txt` dosyaları listelenecektir.
2. Listeden bir dosya numarası seçerek özetlemek istediğiniz metni belirleyin.
3. Özet işlemi tamamlandığında, orijinal metin ve özet tablo olarak görüntülenir.
4. Özeti kaydetme seçeneği sunulur; kaydedildiği takdirde dosya belirtilen isimle kaydedilir.
5. Devam etmek isteyip istemediğiniz sorulur.

## Nasıl Çalışır?
1. **Kelime Frekansı Hesaplama**: Metindeki her kelimenin frekansını sayarak bir skorlama yapılır.
2. **Cümle Skorlama**: Kelimelerin frekansına göre cümleler puanlanır.
3. **Özet Çıkarma**: En yüksek skorlu cümleler sıralanarak özet oluşturulur.

## Örnek Çıktı
```plaintext
Orijinal Metin:
Lorem ipsum dolor sit amet, consectetur adipiscing elit...
...
Özet:
Lorem ipsum dolor sit...
```
