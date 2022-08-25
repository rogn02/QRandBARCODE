import pyqrcode 
import png 
from pyqrcode import QRCode 
import barcode
from barcode.writer import ImageWriter

def MakeQR(url_input,extension_of_qr,qr_file_name):
  try:
    url = pyqrcode.create(url_input)
    if extension_of_qr=="png":
      url.png(qr_file_name+'.png', scale = 6)
    else:
      url.svg(qr_file_name+'.svg', scale = 8)
  except:
    print("There has been an error:\n*Recheck your input\n*Check your module installations")

def MakeBarcode(Input_String,Format):
  try:
    barcode_format = barcode.get_barcode_class(Format)
    The_barcode = barcode_format(Input_String, writer=ImageWriter())
    The_barcode.save("generated_barcode")
  except:
    print("There has been an error:\n*Recheck your input\n*Check your module installations")
    
