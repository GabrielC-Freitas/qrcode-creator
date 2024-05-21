import qrcode
from PIL import Image

def gerar_qr_code(texto):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    return img

def main():
    texto = input("Digite o texto ou URL para gerar o QR Code: ")
    img = gerar_qr_code(texto)
    img.show()
    img.save("qr_code.png")
    print("QR Code salvo como 'qr_code.png'.")

if __name__ == "__main__":
    main()
