
# 7-Zip Güncelleme Kontrolü - PyQt5 Uygulaması

Bu Python uygulaması, Windows bilgisayarlarında yüklü olan **7-Zip** sürümünü kontrol eder, resmi 7-Zip web sitesinden güncel sürümü alır ve eğer güncel sürüm mevcutsa, kullanıcıya güncelleme yapma seçeneği sunar. Kullanıcı "Evet" derse, uygulama 7-Zip'i indirip otomatik olarak kurar.

## Özellikler

- Yüklü 7-Zip sürümünü kontrol etme
- Resmi 7-Zip web sitesinden güncel sürümü alma
- Kullanıcıya güncelleme olup olmadığını bildirme
- Güncelleme yapılmasını sağlamak için indirme ve kurulum işlemi
- Kullanıcı dostu, modern PyQt5 tabanlı GUI arayüzü
- 7-Zip simgesi ve renkli modern tasarım

## Gereksinimler

- Python 3.x
- PyQt5
- Requests

### Gereksinimleri Yüklemek İçin:
Projenin bağımlılıklarını yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

## Kullanım

1. **Projeyi İndirin ve Yükleyin**:
   - GitHub deposunu klonlayın veya ZIP olarak indirin.
   
   ```bash
   git clone https://github.com/kullaniciadi/7zip-updater.git
   ```

2. **7zip.ico** Simge Dosyasını İndirin:
   - 7-Zip'in simgesini [7zip.ico](https://link-to-icon.com/7zip.ico) olarak indirip, proje dizinine yerleştirin.

3. **Uygulamayı Başlatın**:
   - Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

   ```bash
   python main.py
   ```

4. **Arayüz**:
   - Uygulama açıldığında, yüklü olan 7-Zip sürümünü kontrol eder ve güncel sürüm olup olmadığını gösterir.
   - Eğer güncel sürüm yoksa, "Güncellemeyi İndir ve Kur" butonuna basarak otomatik olarak güncellemeyi indirebilir ve kurabilirsiniz.

## Exe Halini İndirme
   - [7zip Güncelleyici](https://drive.google.com/file/d/1Gb2JZSASql_zMtX5M8dTwwyABi-_Ay6J/view?usp=sharing) olarak indirip, proje dizinine yerleştirin. 

## Lisans

Bu proje, **MIT Lisansı** altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

- Proje sahibinin iletişim bilgileri: [ebubekirstt](https://twitter.com/ebubekirstt)
- E-posta: ebubekirbastama@gmail.com
