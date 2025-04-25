import qrcode
import webbrowser
import os

QR_CODE_FILE = "qr_code.png"

def generate_qr_code(url: str):
    qr = qrcode.make(url)
    qr.save(QR_CODE_FILE)
    print(f"\nScan this QR code on your phone:\n{url}")
    webbrowser.open(f"file://{os.path.abspath(QR_CODE_FILE)}")

