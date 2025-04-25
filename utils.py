import socket

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'

def get_access_url(NGROK_URL):
    if NGROK_URL:
        print("Using predefined Ngrok URL...")
        return NGROK_URL
    else:
        ip = get_local_ip()
        return f"http://{ip}:1000"
