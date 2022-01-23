# WiFiQR-Core

Generate a QR code to share WiFi creds (SSID+Pass).

this is the core functionality, a library/API used by the WiFiQR WebApp.

<br>
<br>

# Example

Install and use on your own projects.

> Following exmaple shows how to creat an `img.png` containing a QR-Code with your WiFi creditionals.

1. install the lib:

   ```bash
   pip install qrcode
   pip install wifiqr-core
   ```

2. import the lib:

   ```python
   import wifi_qr as wq

   # change this to the desired output image name.
   my_img = "QR_CODE"

   wifi_info = wq.get_wifi()
   qr_img = wq.get_qr(wifi_info)

   # Save the qrcode as .png img in local dir
   qr_img.save(my_img + " .png")
   ```

<br>
<br>

# 👨‍💻 Dev

If you would like to develop the project...

## ☁️ Instalation

### you need

- python 3
- pipenv `pip install --user pipenv`. 

### Start developing

- clone the repo (or better fork it):

  ```shell
  git clone https://github.com/MoElaSec/WiFiQR_Core
  cd WiFiQR_Core
  ```

- install requirments:

  ```shell
  pipenv install
  ```
    > If you don't have pipenv (high recommend you do), A requirments.txt file is provided use:
        `pip install -r requirments.txt` instead.

<br>

## 🧐 How it works

1. Get connected WLAN/WiFi creditionals (SSID+Password)

2. Generte a QR-code from WiFi creds.

### Extras

- Create a Web-UI:
  - Show generated QR-code.
  - Copy+Print button for QR-code.
- Create a Desktop-UI.

## 🛠 Tools

- Python 3
- QRcode: `pip install qrcode`

### extras tools

- Web-UI:
  - Flask & Jinja.
  - HTML5, CSS3 & JS.
  - TailwindCSS.
- Desktop-UI:
  - pyQT
