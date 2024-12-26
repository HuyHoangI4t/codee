from PIL import Image, ImageEnhance
import tkinter as tk

# Bộ ký tự ASCII chi tiết
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{[]}?-_+~<>i!lI;:,\"^`'. "

def resize_image(image, new_width=100):
    """Thay đổi kích thước hình ảnh, giữ nguyên tỷ lệ"""
    width, height = image.size
    aspect_ratio = height / width / 2.0  # Điều chỉnh tỷ lệ để phù hợp ký tự ASCII
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_image

def enhance_image(image):
    """Tăng cường độ sáng và độ tương phản của hình ảnh"""
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.5)  # Tăng độ sáng (1.0 là mặc định)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.5)  # Tăng độ tương phản
    return image

def grayify(image):
    """Chuyển hình ảnh sang thang độ xám"""
    return image.convert("L")

def pixels_to_ascii(image):
    """Chuyển các pixel thành ký tự ASCII"""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[int(pixel / 255 * (len(ASCII_CHARS) - 1))] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Chuyển hình ảnh thành ASCII art"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Không mở được hình ảnh: {e}"

    # Tăng cường chất lượng hình ảnh
    image = enhance_image(image)
    
    # Thay đổi kích thước và chuyển thành grayscale
    image = resize_image(image, new_width)
    grayscale_image = grayify(image)
    
    # Chuyển đổi pixel sang ký tự ASCII
    ascii_str = pixels_to_ascii(grayscale_image)
    
    # Sắp xếp ASCII art thành các dòng
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    return ascii_image

def show_ascii_in_window(ascii_art):
    """Hiển thị ASCII art trong một cửa sổ tkinter, vừa kích thước"""
    root = tk.Tk()
    root.title("ASCII Art Viewer")

    # Tính kích thước tối ưu của cửa sổ
    lines = ascii_art.split("\n")
    max_width = max(len(line) for line in lines)
    num_lines = len(lines)

    # Cài đặt kích thước cửa sổ (mỗi ký tự = 8 pixel rộng, 16 pixel cao)
    window_width = max_width * 7
    window_height = num_lines * 14
    root.geometry(f"{window_width}x{window_height}")

    # Tạo widget Text để hiển thị ASCII art
    text_widget = tk.Text(root, wrap=tk.NONE, font=("Courier", 8))
    text_widget.insert(tk.END, ascii_art)
    text_widget.config(state=tk.DISABLED)  # Không cho chỉnh sửa nội dung
    text_widget.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

# Đường dẫn đến hình ảnh
image_path = "image.png"  # Thay bằng đường dẫn đến hình ảnh của bạn

# Chuyển hình ảnh thành ASCII art
ascii_art = image_to_ascii(image_path, new_width=100)

# Hiển thị ASCII art trong cửa sổ
show_ascii_in_window(ascii_art)
