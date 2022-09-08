# QR and Barcode generator
This python program has two functions which allows you to create both QRs and barcodes. It is easy to use and comes with error handling.

## Required modules:
 pip install pyqrcode
 pip install pypng
 pip install python-barcode
 

## The two functions are:

i) MakeQR
  It makes a QR of the input URL and saves it as a PNG or a SVG.
  inputs:
  url_input: your URL
  extenstion_of_qr: here you enter "png" or "svg"
  qr_file_name: here you enter the name of the QR file 

ii) MakeBarcode
   It makes a barcode of the input string(numeric or alpha numeric based on format).
   inputs:
   Input_String: The numeric or alphanumeric input string which hastobe converted to a barcode.
   Format: The format you want for the barcode gen.
  
 ## Reference:
 
 barcode formats for your input string: https://python-barcode.readthedocs.io/en/latest/supported-formats.html

