import qrcode
import sys

def generate_qr_code(data, filename='qrcode.png'):
    # Cria uma instância do gerador QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Adiciona o dado ao QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Cria a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')
    
    # Salva a imagem (sobrescreve o arquivo existente)
    img.save(filename)
    print(f'QR Code salvo como {filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python generate_qrcode.py <link>")
        sys.exit(1)

    link = sys.argv[1]
    generate_qr_code(link)