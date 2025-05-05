import pyautogui
import socket

# Fail-Safe özelliğini devre dışı bırakıyoruz
pyautogui.FAILSAFE = False

# Sunucu oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.46', 12345))  # IP adresini ve portu güncelleyin
server_socket.listen(1)

print("Sunucu başlatıldı. Bağlantı bekleniyor...")
client_socket, client_address = server_socket.accept()
print("Bağlantı sağlandı:", client_address)

try:
    while True:
        # Veriyi al ve decode et
        data = client_socket.recv(1024).decode("utf-8").strip()
        
        # Gelen veri varsa işleme devam et
        if data:
            print("Gelen veri:", data)
            
            if data.startswith("MOVE"):
                # Komutu ve koordinatları ayır ve doğrula
                parts = data.split(",")
                
                if len(parts) == 3:  # Beklenen format: 'MOVE,x,y'
                    _, x_str, y_str = parts
                    try:
                        x, y = float(x_str), float(y_str)
                        
                        # İmleci hareket ettir
                        pyautogui.moveTo(x, y)
                    except ValueError:
                        print("Koordinatlar sayıya çevrilemedi:", x_str, y_str)
                else:
                    print("Geçersiz MOVE komutu formatı:", data)
            
            elif data == "CLICK":
                # Tıklama komutu geldiyse tıkla
                pyautogui.click()

except Exception as e:
    print("Bir hata oluştu:", e)
finally:
    client_socket.close()
    server_socket.close()
