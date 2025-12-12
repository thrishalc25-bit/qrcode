import qrcode
hello=input("enter the value to conver it into qrcode")
code=qrcode.make(hello)
code.save("qr.jpg")
print("done")