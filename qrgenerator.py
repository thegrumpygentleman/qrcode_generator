import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    # Get input text from the entry widget
    input_text = entry.get()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code image
    qr_img = qr_img.resize((200, 200))
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Create input entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=5)

# Create label for displaying QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
