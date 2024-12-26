import qrcode

# Dữ liệu muốn mã hóa
data = "https://www.youtube.com/results?search_query=rick+roll"

# Tạo QR Code
qr = qrcode.QRCode(
    version=2,  # Kích thước mã QR, 1 là nhỏ nhất (21x21), càng lớn càng chứa được nhiều dữ liệu
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Mức độ sửa lỗi
    box_size=10,  # Kích thước mỗi ô vuông trong QR
    border=2,  # Viền (mặc định là 4)
)
qr.add_data(data)
qr.make(fit=True)

# Tạo hình ảnh
img = qr.make_image(fill_color="black", back_color="white")

# Lưu hình ảnh
img.save("qrcode.png")
print("QR code đã được tạo và lưu thành công!")
