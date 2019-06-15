import qrcode
import androidhelper.sl4a as android
droid = android.Android()
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Fbi movie')
qr.make(fit=True)

img = qr.make_image()
img.save("/sdcard/out.jpg")
droid.view("file:///sdcard/out.jpg","image/*")