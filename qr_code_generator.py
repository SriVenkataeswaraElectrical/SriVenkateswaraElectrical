import qrcode

link = "https://srivenkataeswaraelectrical.github.io/SriVenkateswaraElectrical/product_images/main.html?image=image1.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code.png")

print("QR Code generated successfully.")

