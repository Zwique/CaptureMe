# Cybersecurity Photo Capture App

This is a **cybersecurity-focused web application** built using **Flask**, designed to allow anyone to capture photos of users directly from their mobile devices and securely upload them to a server. The app leverages **Ngrok** for secure tunneling, exposing the local server to the public internet via an encrypted tunnel. Additionally, **QR codes** are generated for easy access to the public URL, making the app both secure and convenient to use.

This project serves as an example of how to handle **secure file uploads** and **remote access** within a web application, with a focus on **data security** and **privacy**.

## Features

- **Photo Capture from Mobile Devices**: The application allows anyone to capture photos of users using their mobile device's camera and upload them to the server via a web interface.
- **Ngrok Integration for Secure Tunneling**: By integrating Ngrok, the app creates a secure, encrypted tunnel from your local Flask server to the public internet, enabling remote access to the app while maintaining security.
- **Automatic QR Code Generation**: Each time the app is run, a QR code is automatically generated containing the public Ngrok URL, making it easy to share the URL and access the app from mobile devices.
- **Secure File Upload**: Only images in specific formats (e.g., JPG, PNG) can be uploaded to the server. This helps prevent malicious file uploads and ensures that only valid files are saved on the server.
- **Incremental File Naming**: Uploaded photos are saved with unique incremental filenames inside `/photos` directory (e.g., `captured_photo1.jpg`, `captured_photo2.jpg`) to prevent overwriting and ensure no data is lost.
- **Remote Access and QR Code Sharing**: The app generates a public URL via Ngrok, which can be shared with others via the QR code for easy access to the photo capture page.


## Installation Instructions
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

  **⚠️ Warning: Educational Use Only ⚠️**

This project is intended solely for educational purposes. It is not designed for production environments and should not be used for any malicious or unauthorized activities. The application demonstrates basic concepts of web security and file handling. Use responsibly and with permission.
