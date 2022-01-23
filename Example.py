from wifi_qr import wifi_2_qr

# change this to the desired output image name.
img_name = "QR_CODE"

ssid = "your_wifi_name"
password = "your_wifi_pass"

# 🛠 Initialize the class
qr_wifi = wifi_2_qr()

# 🔐 Get WiFi credentials
try:
    my_wifi_info = qr_wifi.get_wifi()
    print(my_wifi_info)
except TypeError:
    "Incase using MacOS, must set the wifi manually"
    my_wifi_info = qr_wifi.set_wifi(
        ssid=ssid, password=password, auth_type='WPA2', hidden="false")
except:
    print("Something wrong accored..!")


# 🎨 Build the QR-Code
qr_img = qr_wifi.get_qr(my_wifi_info)
print(qr_img)


# 💾 Save the qrcode as .png img in local dir
qr_wifi.save_qr(qr_img, img_name)

# or you can:
# qr_img.save(img_name + " .png")
