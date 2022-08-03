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
import re

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

image3 = cv2.imread('more_info.png',cv2.IMREAD_GRAYSCALE)

roi = (1130, 443, 183, 40) #dead
im_dead = image3[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (1130, 668, 183, 40) #rss assistance
im_rss_assistance = image3[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#2nd check for deads with more filters to avoid some errors
roi = (1130, 443, 183, 40) #dead
thresh = 127
thresh_image = cv2.threshold(image3, thresh, 255, cv2.THRESH_BINARY)[1]
im_dead2 = thresh_image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (1130, 668, 183, 40) #rss assistance
im_rss_assistance2 = thresh_image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#3rd check for deads with more filters to avoid some errors
roi = (1130, 443, 183, 40) #dead
blur_img = cv2.GaussianBlur(image3, (3, 3), 0)
im_dead3 = blur_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (1130, 668, 183, 40) #rss assistance
im_rss_assistance3 = blur_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('im_dead.png', im_dead)
cv2.imwrite('im_dead2.png', im_dead2)
cv2.imwrite('im_dead3.png', im_dead3)
cv2.imwrite('im_rss_assistance.png', im_rss_assistance)
cv2.imwrite('im_rss_assistance2.png', im_rss_assistance2)
cv2.imwrite('im_rss_assistance3.png', im_rss_assistance3)

#3rd image data
gov_dead = pytesseract.image_to_string(im_dead,config="-c tessedit_char_whitelist=0123456789")
gov_dead2 = pytesseract.image_to_string(im_dead2,config="-c tessedit_char_whitelist=0123456789")
gov_dead3 = pytesseract.image_to_string(im_dead3,config="-c tessedit_char_whitelist=0123456789")
gov_rss_assistance = pytesseract.image_to_string(im_rss_assistance,config="-c tessedit_char_whitelist=0123456789")
gov_rss_assistance2 = pytesseract.image_to_string(im_rss_assistance2,config="-c tessedit_char_whitelist=0123456789")
gov_rss_assistance3 = pytesseract.image_to_string(im_rss_assistance3,config="-c tessedit_char_whitelist=0123456789")

print('gov_dead: ' + gov_dead + 'gov_dead2: ' + gov_dead2 + 'gov_dead3: ' + gov_dead3)
print('gov_rss_assistance: ' + gov_rss_assistance + 'gov_rss_assistance2: ' + gov_rss_assistance2 + 'gov_rss_assistance3: ' + gov_rss_assistance3)

image = cv2.imread('gov_info.png')
#Power and Killpoints
roi = (775, 230, 244, 38)
im_gov_id = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('im_gov_id.png', im_gov_id)

image = cv2.imread('gov_info.png',cv2.IMREAD_GRAYSCALE)
# image = cv2.GaussianBlur(image, (5, 5), 0)
roi = (890, 364, 170, 44)
im_gov_power = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('im_gov_power.png', im_gov_power)

roi = (1114, 364, 222, 44)
im_gov_killpoints = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imwrite('im_gov_killpoints.png', im_gov_killpoints)

gov_id = pytesseract.image_to_string(im_gov_id,config="-c tessedit_char_whitelist=0123456789")
gov_power = pytesseract.image_to_string(im_gov_power,config="-c tessedit_char_whitelist=0123456789")
gov_killpoints = pytesseract.image_to_string(im_gov_killpoints,config="-c tessedit_char_whitelist=0123456789")

print('gov_id: ' + gov_id + 'gov_power: ' + gov_power + 'gov_killpoints: ' + gov_killpoints);
exit

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

gov_power = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_power)
gov_dead = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_dead)
gov_dead2 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_dead2)
gov_dead3 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_dead3)
gov_killpoints = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_killpoints)
gov_kills_tier1 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_kills_tier1)
gov_kills_tier2 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_kills_tier2)
gov_kills_tier3 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_kills_tier3)
gov_kills_tier4 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_kills_tier4)
gov_kills_tier5 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_kills_tier5)
gov_rss_assistance = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_rss_assistance)
gov_rss_assistance2 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_rss_assistance2)
gov_rss_assistance3 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', gov_rss_assistance3)
print(locals())

print('gov_kills_tier1: ' + gov_kills_tier1 + 'gov_kills_tier2: ' + gov_kills_tier2 + 'gov_kills_tier3: ' + gov_kills_tier3 + 'gov_kills_tier4: ' + gov_kills_tier4 + 'gov_kills_tier5: ' + gov_kills_tier5);

if gov_power == '' or gov_killpoints == '' or gov_dead == '' or gov_kills_tier1 == '' or gov_kills_tier2 == '' or gov_kills_tier3 == '' or gov_kills_tier4 == '' or gov_kills_tier5 == '' or gov_rss_assistance == '':
	cv2.imwrite('im_gov_id.png', im_gov_id)
	cv2.imwrite('im_gov_power.png', im_gov_power)
	cv2.imwrite('im_gov_killpoints.png', im_gov_killpoints)
	cv2.imwrite('im_dead.png', im_dead)
	cv2.imwrite('im_dead2.png', im_dead2)
	cv2.imwrite('im_dead3.png', im_dead3)
	cv2.imwrite('im_rss_assistance.png', im_rss_assistance)
	cv2.imwrite('im_rss_assistance2.png', im_rss_assistance2)
	cv2.imwrite('im_rss_assistance3.png', im_rss_assistance3)
	cv2.imwrite('image2.png', image2)
	cv2.imwrite('im_kills_tier1.png', im_kills_tier1)
	cv2.imwrite('im_kills_tier2.png', im_kills_tier2)
	cv2.imwrite('im_kills_tier3.png', im_kills_tier3)
	cv2.imwrite('im_kills_tier4.png', im_kills_tier4)
	cv2.imwrite('im_kills_tier5.png', im_kills_tier5)
	os.system('pause')
