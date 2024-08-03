import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,
)
qr.add_data("https://github.com/wahaj12569/PythonProjects")
qr.make(fit=True)
img=qr.make_image(
    fill_color="yellow",
    back_color="white"
)
img.save("github1.png")