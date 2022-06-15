'''Importing Different Libraries'''

import pytesseract
from PIL import Image,ImageFilter

'''Converting the image to text'''

def conversion(file):

    pic = Image.open(file)
    imgGray = pic.convert('L')# converting the image to grayscale
    imgGray = imgGray.resize((1191, 2000))# resizing the image
    im2 = imgGray.filter(ImageFilter.UnsharpMask(radius = 6.1, threshold = 10, percent = 172))
    options = '-l eng --oem 3 --psm 4'

    converted_text = pytesseract.image_to_string(im2, config=options)#converting the image into string
    
    return converted_text#returning the text extracted from image