import qrcode

img = qrcode.make("https://shubham1921.pythonanywhere.com/")

img.save("myqr.jpg")