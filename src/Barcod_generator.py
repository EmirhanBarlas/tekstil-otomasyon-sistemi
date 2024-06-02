## Barkod oluşturma işlemlerini yöneten dosya
import barcode
from barcode.writer import ImageWriter

class BarcodeGenerator:
    def __init__(self, barcode_type='code128'):
        self.barcode_type = barcode_type

    def generate_barcode(self, data, output_file):
        BARCODE = barcode.get_barcode_class(self.barcode_type)
        barcode_instance = BARCODE(data, writer=ImageWriter())
        barcode_instance.save(output_file)
        return f"{output_file}.png" # Barkod çıktısını png olarak gönderme işlemi