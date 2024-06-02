from Barcod_generator import BarcodeGenerator
from Database import Database
import os

def main():

    # Barkodları saklamak için klasör oluştur
    if not os.path.exists('barcodes'):
        os.makedirs('barcodes')
    # Excel dosyalarını saklamak için klasör oluştur
    if not os.path.exists('excels'):
        os.makedirs('excels')
    # Yaml dosyalarını saklamak için klasör oluştur
    if not os.path.exists('yamls'):
            os.makedirs('yamls')
    
    # Veritabanı ve barkod oluşturucu nesnelerini başlat
    db = Database('database.db')
    barcode_gen = BarcodeGenerator()

    while True:
        print("\n1. Ürün Ekle")
        print("2. Tedarikçi Ekle")
        print("3. Kumaş Ekle")
        print("4. Kumaşları Görüntüle")
        print("5. Excel Dosyası olarak çıktı al")
        print("6. Yaml Dosyası olarak çıktı al")
        print("7. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == '1':
            product_name = input("Ürün adı: ")
            product_code = input("Ürün kodu (barkod için): ")
            barcode_file = barcode_gen.generate_barcode(product_code, f"barcodes/{product_code}")
            db.add_product(product_name, product_code)
            print(f"Barkod oluşturuldu ve {barcode_file} dosyasına kaydedildi.")
            print(f"{product_name} ürünü veritabanına eklendi.")

        elif choice == '2':
            supplier_name = input("Tedarikçi adı: ")
            contact = input("İletişim bilgileri: ")
            address = input("Adres: ")
            db.add_supplier(supplier_name, contact, address)
            print(f"{supplier_name} tedarikçisi veritabanına eklendi.")

        elif choice == '3':
            supplier_id = int(input("Tedarikçi ID: "))
            fabric_type = input("Kumaş tipi: ")
            quantity = float(input("Miktar (metre): "))
            arrival_date = input("Geliş tarihi (YYYY-MM-DD): ")
            source = input("Kaynak: ")
            db.add_fabric(supplier_id, fabric_type, quantity, arrival_date, source)
            print("Kumaş bilgileri veritabanına eklendi.")

        elif choice == '4':
            fabrics = db.get_all_fabrics()
            for fabric in fabrics:
                print("-" * 20)
                print(f"Kumaş ID: {fabric[0]}")
                print(f"Tedarikçi ID: {fabric[1]}")
                print(f"Kumaş Tipi: {fabric[2]}")
                print(f"Miktar (metre): {fabric[3]}")
                print(f"Geliş Tarihi: {fabric[4]}")
                print(f"Kaynak: {fabric[5]}")
                print("-" * 20)

        elif choice == '5':
            db.export_to_excel()
            print("Excel dosyası oluşturuldu.")

        elif choice == '6':
            db.export_to_yaml()
            print("YAML dosyası oluşturuldu.")

        elif choice == '7':
            break

        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

    # Veritabanı bağlantısını kapat
    db.close()

if __name__ == "__main__":
    main()