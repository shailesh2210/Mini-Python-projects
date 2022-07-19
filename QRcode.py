# Basic Qrcode

from turtle import fillcolor
from matplotlib.pyplot import fill
import qrcode as qr
from regex import F
img = qr.make("https://www.instagram.com/mr____gaddam/")
img.save("Shailesh_Instagram.png")

# Advance Qrcode

import qrcode as qr
from PIL import Image

code = qr.QRCode(version=1 , error_correction= qr.ERROR_CORRECT_M, box_size=10 , border=3)
code.add_data("https://www.onehack.us")
code.make(fit=True)
img = code.make_image(fill_color = "Black" , back_color = "white")
img.save("onehack.png")
