import socket
import time  # Gecikme eklemek için kullanılacak
import pyautogui

# Ekran boyutlarını al
screen_width, screen_height = pyautogui.size()  # Ekran boyutlarını al

# Sunucu ayarları
HOST = '127.0.0.1'  # Sunucunun IP adresi
PORT = 12345        # Sunucunun portu

# Sunucuya bağlanma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # İmleci taşımak için komut gönder
    x, y = 100, 100  # Hedef koordinatlar (x, y)

    # Ekran boyutlarını aşmamak için x ve y değerlerini kontrol et
    x = min(max(x, 0), screen_width)  # Ekranın dışına çıkmamak için x koordinatını sınırla
    y = min(max(y, 0), screen_height)  # Ekranın dışına çıkmamak için y koordinatını sınırla

    command = f"MOVE,{x},{y}".strip()  # strip() ile boşluk ve yeni satır karakterlerini temizleyin
    s.sendall(command.encode('utf-8'))
    time.sleep(1)  # Komutlar arasında kısa bir gecikme

    # Tıklama komutu gönder
    command = "CLICK"
    s.sendall(command.encode('utf-8'))
