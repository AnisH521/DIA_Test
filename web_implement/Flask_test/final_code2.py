'''Importing Different Libraries'''

import pytesseract
from PIL import Image,ImageFilter

'''Converting the image to text'''

'''radius'''
#The Radius setting controls how many neighboring pixels around high-contrast edges the filter affects.
# When setting a value, consider the pixel count of the image and its subject matter. 
# The higher the pixel count, the higher the Radius value needed

'''thresold'''
#Choose a Threshold value to establish how different in value an area of pixels must be from an adjacent area for it to be affected by the filter.
#Start with a Threshold value of 0 (to sharpen the entire image), then increase it gradually
# At a Threshold of 5–10, high-contrast areas will be sharpened and areas of lesser contrast will be sharpened much less

'''percent'''
# percentage to control how much the contrast will be increased.

'''options , psm 4'''
#using --psm 4 is when you need to OCR column data and require 
# text to be concatenated row-wise (e.g., the data you would find in a spreadsheet, table, or receipt)


def conversion(file):

    pic = Image.open(file)
    imgGray = pic.convert('L')# converting the image to grayscale
    imgGray = imgGray.resize((1191, 2000))# resizing the image
    im2 = imgGray.filter(ImageFilter.UnsharpMask(radius = 6.1, threshold = 10, percent = 172))
    options = '-l eng --oem 3 --psm 4'

    converted_text = pytesseract.image_to_string(im2, config=options)#converting the image into string
    
    return converted_text#returning the text extracted from image
