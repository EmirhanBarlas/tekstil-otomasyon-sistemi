from database import Database
from Barcod_generator import BarcodeGenerator
import os

def main():
    if not os.path.exists('barcodes'):
        os.makedirs('barcodes')
    db = Database('products.db')
    barcode_gen = BarcodeGenerator()
    product_name = input("Ürün adı: ")
    product_code = input("Ürün kodu (barkod için): ")
    barcode_file = barcode_gen.generate_barcode(product_code, f"barcodes/{product_code}")
    db.add_product(product_name, product_code)
    print(f"Barkod oluşturuldu ve {barcode_file} dosyasına kaydedildi.")
    print(f"{product_name} ürünü veritabanına eklendi.")
    db.close()

if __name__ == "__main__":
    main()
