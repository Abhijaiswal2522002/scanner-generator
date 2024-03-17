import qrcode

# Create instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Data to encode
data = "https://www.linkedin.com/in/abhishek-jaiswal-278890246/"

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it
img.save("qrcode.png")
# img.show()  # Uncomment this line to display the image
