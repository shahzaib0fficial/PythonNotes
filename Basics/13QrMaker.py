#pip install qrcode
import qrcode

img = qrcode.make("https://github.com/shahzaib0fficial")

img.save("qr.png","PNG")