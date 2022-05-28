'''Importing Different Libraries'''

import cv2
import pytesseract

path = '/home/anish/Documents/data_test/418S3TgVd-L.jpg'

'''Converting the image to text'''

def conversion(file):
    
    pic = cv2.imread(file)#the method is used to load image as Numpy array
    
    pic = cv2.resize(pic, None, fx=2, fy=2)#resizing the image for better string conversion
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)#cvtColor method for channel conversion
    
    converted_text = pytesseract.image_to_string(pic, lang='eng')#converting the image into string
    
    return converted_text#returning the text extracted from image

print(conversion(path))