from ppadb.client import Client
import cv2
import sys
import os
from PIL import Image
import pytesseract
import numpy as np
import time
from matplotlib import pyplot as plt
import xlwt 
from xlwt import Workbook
from datetime import date
import tkinter as tk
import keyboard

def tointcheck(element):
	try:
		return int(element)
	except ValueError:
		return element
	
#Initiliaze paths and variables
today = date.today()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Change to your installation path folder.

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
os.system("")

image2 = cv2.imread('kills_tier.png',cv2.IMREAD_GRAYSCALE)
roi = (860, 595, 215, 28) #tier 1
im_kills_tier1 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

roi = (861, 640, 215, 26) #tier 2
im_kills_tier2 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

roi = (861, 685, 215, 26) #tier 3
im_kills_tier3 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

roi = (861, 730, 215, 26) #tier 4
im_kills_tier4 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

roi = (861, 775, 215, 26) #tier 5
im_kills_tier5 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('im_kills_tier5.png', im_kills_tier5)

#2nd image data
gov_kills_tier1 = pytesseract.image_to_string(im_kills_tier1,config="-c tessedit_char_whitelist=0123456789")
gov_kills_tier2 = pytesseract.image_to_string(im_kills_tier2,config="-c tessedit_char_whitelist=0123456789")
gov_kills_tier3 = pytesseract.image_to_string(im_kills_tier3,config="-c tessedit_char_whitelist=0123456789")
gov_kills_tier4 = pytesseract.image_to_string(im_kills_tier4,config="-c tessedit_char_whitelist=0123456789")
gov_kills_tier5 = pytesseract.image_to_string(im_kills_tier5,config="-c tessedit_char_whitelist=0123456789")

print('gov_kills_tier1: ' + gov_kills_tier1 + 'gov_kills_tier2: ' + gov_kills_tier2 + 'gov_kills_tier3: ' + gov_kills_tier3 + 'gov_kills_tier4: ' + gov_kills_tier4 + 'gov_kills_tier5: ' + gov_kills_tier5);
exit
