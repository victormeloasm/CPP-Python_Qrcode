import sys
import os
import qrcode
from PIL import Image

def generate_qr_code(data, output_file):
    # Remove o arquivo se ele já existir
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Cria uma instância do gerador de QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Adiciona os dados ao QR Code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Cria a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')
    
    # Salva a imagem no arquivo especificado
    img.save(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python gqrcode.py <texto> <output_file>")
        sys.exit(1)
    
    data = sys.argv[1]
    output_file = sys.argv[2]
    
    # Gera o QR Code
    generate_qr_code(data, output_file)
