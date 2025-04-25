# 📸 Cybersecurity Photo Capture App

This is a **cybersecurity-focused web application** built using **Flask**, designed to allow anyone to capture photos of users directly from their mobile devices and securely upload them to a server. The app leverages **Ngrok** for secure tunneling, exposing the local server to the public internet via an encrypted tunnel. Additionally, **QR codes** are generated for easy access to the public URL, making the app both secure and convenient to use.

This project serves as an example of how to handle **secure file uploads** and **remote access** within a web application, with a focus on **data security** and **privacy**.

## 🔥 Features  
- **Mobile Photo Capture** – Take photos using a device's camera and upload secretly.  
- **Ngrok Secure Tunneling** – Expose your local server via an encrypted public URL.  
- **QR Code Access** – Auto-generated QR code for instant mobile connectivity.  
- **Secure Uploads** – Only allows JPG/PNG files with incremental filenames (e.g., `captured_photo1.jpg`).  
- **Local Storage** – Files saved in `/photos` (no cloud dependency).  

## 🚀 Quick Start  


### Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/zwique/CaptureMe.git
   cd cybersecurity-photo-capture-app
   ```
2. **Set up a Virtual Environment (optional but recommended):**
   - It's a good practice to create a virtual environment to isolate your project dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate  # Windows
    ```
### Before running the application, ensure you have the following installed:

3. **Install Ngrok**:
   - Ngrok is a tool that creates a secure tunnel to your local development environment, making your Flask app accessible over the internet. It is required to expose the local Flask server to the outside world.
   - You can download and install Ngrok from [ngrok.com](https://ngrok.com/).

4. **Install Dependencies**:
   - The Python dependencies for this project are listed in the `requirements.txt` file. You can install them by running the following command:
   ```bash
   pip3 install -r requirements.txt
    ```
5. **Run:**
   ```
   python app.py
   ```
6. **Access**:
   - Scan the QR code on your phone to open the app. Then, grant the necessary permissions to allow the app to capture a photo using your phone's front camera.
8. **Check Saved Photos**:
   - Once a photo is captured, it will be uploaded to the server and saved in the photos/ directory with an incremented filename (e.g., captured_photo1.jpg, captured_photo2.jpg, etc.).

  **⚠️ Warning: Educational Use Only**

This project is intended solely for educational purposes. It is not designed for production environments and should not be used for any malicious or unauthorized activities. The application demonstrates basic concepts of web security and file handling. Use responsibly and with permission.
