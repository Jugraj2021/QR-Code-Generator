import qrcode

def generate_qr_code(text, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill="black", back_color="white")

    # Save the image to a file
    img.save(filename)

# Example usage
text = "Hello, World!"
filename = "qr_code.png"
generate_qr_code(text, filename)
print(f"QR code saved to {filename}")
