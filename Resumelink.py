import qrcode

# Link to your resume
data = "https://drive.google.com/file/d/14hnOJfS6au0RqGX__TUg6DwSu_iYzJMY/view?usp=sharing"  # Replace with your actual link
#https://drive.google.com/file/d/14hnOJfS6au0RqGX__TUg6DwSu_iYzJMY/view?usp=sharing
# Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# Save the QR Code
img.save("resume_qrcode.png")
print("QR code for your resume has been saved as 'resume_qrcode.png'")