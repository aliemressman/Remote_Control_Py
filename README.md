# Python Remote Mouse Control 🖱️💻

Python ile geliştirilmiş, yerel ağ üzerinden bir bilgisayara bağlanarak **mouse imlecini uzaktan kontrol etmeyi** sağlayan basit bir uzaktan kontrol sistemi.

📌 **Bu proje, socket programlama ve sistem otomasyonu üzerine pratik yapmak amacıyla geliştirilmiştir.**

## 🧠 Proje Özeti

Bu sistem iki ana bileşenden oluşur:

- **Server (Sunucu):** Kontrol edilecek bilgisayarda çalışır. Gelen komutları alır ve uygular.
- **Client (İstemci):** Mouse hareketlerini ve tıklama komutlarını gönderir.

## 🚀 Özellikler

- 🎮 Mouse imlecini X ve Y ekseninde hareket ettirme
- 🖱️ Sol ve sağ tıklama desteği
- 🔌 LAN üzerinden iletişim (TCP soket)
- 🪟 Basit bir grafik arayüz (isteğe bağlı)
- 🐍 `pyautogui` ile doğrudan sistem kontrolü

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **socket** – Ağ iletişimi
- **pyautogui** – Mouse ve klavye kontrolü
- **Tkinter** (opsiyonel) – Arayüz

## 📦 Kurulum

1. Depoyu klonla:

```bash
git clone https://github.com/aliemressman/python-remote-mouse.git
cd python-remote-mouse
