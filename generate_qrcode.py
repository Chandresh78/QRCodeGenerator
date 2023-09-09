import qrcode

# Define your LinkedIn profile URL
linkedin_url = "https://www.linkedin.com/in/chandreshrajpoot/"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in the QR code
    border=4,     # Border width around the QR code
)

# Add the LinkedIn URL to the QR code
qr.add_data(linkedin_url)
qr.make(fit=True)

# Create an image from the QR code with yellow background and green QR code
img = qr.make_image(fill_color="green", back_color="yellow")

# Save the image to a file
img.save("LinkedInQRCode.png")

# Display the QR code (optional)
img.show()
