import os

import qrcode

data = 'https://t.me/WakeUpNeoo'

filename = input("задайте имя qr code с расширением png")
img = qrcode.make(data)
img.save(filename)

if filename == 'qr2.png':
    os.remove(filename)
    print('QR code(duplicate) removed to ' + filename)
