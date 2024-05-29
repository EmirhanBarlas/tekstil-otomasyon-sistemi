# Tekstil Otomasyon Sistemi

Tekstil Otomasyon Sistemi, tekstil atölyeleri için geliştirilmiş bir otomasyon yazılımıdır. Bu sistem, ürün yönetimi, stok takibi, sipariş yönetimi ve raporlama gibi temel işlevleri içerir.

## Özellikler

- **Ürün Yönetimi:** Ürünlerin isimleri, barkodları ve stok miktarları gibi bilgileri yönetebilirsiniz.
- **Stok Takibi:** Stoktaki ürün miktarlarını izleyebilir ve güncelleyebilirsiniz.
- **Sipariş Yönetimi:** Müşteri siparişlerini alabilir, işleyebilir ve takip edebilirsiniz.
- **Kumaş Yönetimi:** Kumaşların kimden, nereden, ne zaman geldiği ve kaç metre olduğu gibi bilgileri yönetebilirsiniz.
- **Tedarikçi Yönetimi:** Tedarikçi bilgilerini yönetebilir ve izleyebilirsiniz.
- **Raporlama:** Satış raporları, stok durumu raporları gibi çeşitli raporlar oluşturabilirsiniz.

## Kurulum

1. Projeyi klonlayın:

    ```bash
    git clone https://github.com/EmirhanBarlas/tekstil-otomasyon-sistemi.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd tekstil-otomasyon-sistemi
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Veritabanını oluşturun:

    ```bash
    python setup.py
    ```

## Dosya Yapısı

```plaintext
tekstil-otomasyon-sistemi/
│
├── barcodes/                    # Barkod görüntü dosyalarının saklandığı dizin
│
├── src/                         # Kaynak dosyalarının bulunduğu dizin
│   ├── database.py              # Veritabanı işlemlerini yöneten dosya
│   ├── barcode_generator.py     # Barkod oluşturma işlemlerini yöneten dosya
│   └── main.py                  # Ana çalışma dosyası
│
├── .gitignore                   # Git için ihmal edilecek dosyaların listesi
├── LICENSE                      # Lisans dosyası
├── README.md                    # Proje açıklamaları içeren bu dosya
└── requirements.txt             # Gerekli Python paketlerini içeren dosya

## Kullanım

1. Ana dosyayı çalıştırın:

    ```bash
    python main.py
    ```

2. Konsol penceresinde yönergeleri takip edin ve ürünleri, stokları, siparişleri yönetin.

## Katkıda Bulunma

1. Bu depoyu (`fork`) klonlayın.
2. Yeni özellikler veya hatalar düzeltebilirsiniz.
3. Değişikliklerinizi gönderin (`commit`) ve bir çekme isteği (`pull request`) açın.
