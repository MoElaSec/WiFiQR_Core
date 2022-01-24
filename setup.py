# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

MINIMAL_DESCRIPTION = """# WiFiQR-Core

Generate a QR code to share WiFi creds (SSID+Pass).

this is the core functionality, a library/API used by the WiFiQR WebApp.

<br>
<br>

# Usage

1. install the lib:

   ```bash
   pip install Pillow
   pip install qrcode
   pip install wifiqr-core
   ```

2. Varouise ways to use:

   - Import as a lib or an API:

     ```python
     from wifiqr_core import wifi_2_qr

     # Initialize the class
     wq = wifi_2_qr()
     ```

   - CLI tool:
     ```shell
     $ wifiqr_core
     As a MacOS user, you gotta fill in manually...
     WiFi Name: ******
     Hidden Network (yes/no): no
     WiFi Password (leave empty if none): **********
     Output/image name: qr
     ```

## Example

Install and use on your own projects.

> Following exmaple shows how to creat an `img.png` containing a QR-Code with your WiFi creditionals.

```python
from wifiqr_core import wifi_2_qr

# change this to the desired output image name.
img_name = "QR_CODE"

ssid = "your_wifi_name"
password = "your_wifi_pass"

# Initialize the class
wq = wifi_2_qr()

# Get WiFi credentials
try:
    my_wifi_info = wq.get_wifi()
    print(my_wifi_info)
except TypeError:
    "Incase using MacOS, must set the wifi manually"
    my_wifi_info = wq.set_wifi(
        ssid=ssid, password=password, auth_type='WPA2', hidden="false")
except:
    print("Something wrong accored..!")


# Build the QR-Code
qr_img = wq.get_qr(my_wifi_info)
print(qr_img)


# Save the qrcode as .png img in local dir
wq.save_qr(qr_img, img_name)

# or you can:
# qr_img.save(img_name + " .png")
```

<br>
<br>

# Dev

If you would like to develop the project...

## Instalation

### you need

- python 3 & pip.
- pipenv `pip install --user pipenv`.
- qrcode `pip install qrcode`.
- Pillow `pip install Pillow`.

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
<br>

## How it works

1. Get connected WLAN/WiFi creditionals (SSID+Password)

2. Generte a QR-code from WiFi creds.

### Extras

- Create a Web-UI:
  - Show generated QR-code.
  - Copy+Print button for QR-code.
- Create a Desktop-UI.

<br>

## Tools

- Python 3
- QRcode: `pip install qrcode`

### extras tools

- Web-UI:
  - Flask & Jinja.
  - HTML5, CSS3 & JS.
  - TailwindCSS.
- Desktop-UI:
  - pyQT"""


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md", "r") as r:
            description = "\n"
            description += r.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION


setup(
    name='wifiqr-core',

    version='1.0',

    description='An API to generate a QR-code for your WiFI to let others quickly connect.',
    long_description=read_description(),
    long_description_content_type="text/markdown",

    url='https://github.com/MoElaSec/WiFiQR_Core',

    author='Mo Eltahir',
    author_email='mohd.debrecen@gmail.com',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Operating System :: OS Independent',

        'Topic :: Communications',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering'
    ],

    keywords=['WiFi', 'qrcode', 'pillow'],

    py_modules=['wifiqr_core'],

    install_requires=['Pillow', 'qrcode'],

    entry_points={
        'console_scripts': [
            'wifiqr-core=wifiqr_core:main',
        ]
    },

    packages=find_packages('src'),
    package_dir={'': 'src'},

    test_suite='setup.test_suite',
)
