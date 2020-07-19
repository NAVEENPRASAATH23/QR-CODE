import qrcode

code=qrcode.QRCode(version=10,box_size=15,border= 5 )
  
link=input("Copy the content:")
code.add_data(link)
code.make(fit=True)
img=code.make_image(fill="Red", back_color="pink")
img.save(input("Enter the Qrcode name:")+".png")