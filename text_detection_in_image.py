import cv2
import pytesseract as tess
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import easygui 
import os 
from tkinter import Tcl


# Split PDF into Individual Pages 
# input_pdf = PdfFileReader(open('CIAHologramDocument.pdf', 'rb'))
# for i in range(input_pdf.numPages):
#     output = PdfFileWriter()
#     output.addPage(input_pdf.getPage(i))
#     with open('document-pages%s.pdf' % i, 'wb') as outputStream:
#         output.write(outputStream)
#     print(outputStream)
    

# easygui.egdemo()

# I'm sure there's a better way to do this, but I manually converted each selected pdf to a png with this code
# documentSelection = easygui.fileopenbox()
# images = convert_from_path(documentSelection)
# for image in images:
#     image.save('page.png')




path = '/Users/jacobstephens/Desktop/Code/WebScraping'
fileList = [file for file in os.listdir(path) if file.endswith('.png')]
fileList = sorted(fileList,key=lambda x: int(os.path.splitext(x)[0]))

# print(fileList)
f = open('wholeDoc.txt', 'w')

for file in fileList:
    img = Image.open(file)
    text = tess.image_to_string(img)
    print(text)
    f.write(text)
    
f.close()

