import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='wifiqr-core',

    version='0.1',

    description='An API to generate a QR-code for your WiFI to let others quickly connect.',
    long_description=LONG_DESCRIPTION,

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

    py_modules=['wifiqr-core'],

    install_requires=['Pillow', 'qrcode'],

    entry_points={
        'console_scripts': [
            'wifiqr-core=wifi_qr:main',
        ]
    },

    test_suite='setup.test_suite'
)
