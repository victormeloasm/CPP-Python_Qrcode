import sys
import os
import qrcode
from PIL import Image

def generate_qr_code(data, output_file):

    if os.path.exists(output_file):
        os.remove(output_file)
    
   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
  
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python gqrcode.py <texto> <output_file>")
        sys.exit(1)
    
    data = sys.argv[1]
    output_file = sys.argv[2]

    generate_qr_code(data, output_file)
