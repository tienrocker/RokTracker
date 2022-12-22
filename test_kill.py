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

# get int value default 0
def convertToInt(element):
	try:
		return int(element)
	except ValueError:
		return 0

# get int value from image
debug = True
def image_to_string(img, name = 'img'):
	val = pytesseract.image_to_string(img, config="-c tessedit_char_whitelist=0123456789")
	val = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', val)
	val = convertToInt(val)
	
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	thresh_image = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	val2 = pytesseract.image_to_string(thresh_image, config="-c tessedit_char_whitelist=0123456789")
	val2 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', val2)
	val2 = convertToInt(val2)
	
	blur_img = cv2.GaussianBlur(gray_image, (5, 5), 0)
	val3 = pytesseract.image_to_string(blur_img, config="-c tessedit_char_whitelist=0123456789")
	val3 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff-\n]', '', val3)
	val3 = convertToInt(val3)

	# if debug:
	# 	cv2.imwrite(name + '1.png', img)
	# 	cv2.imwrite(name + '2.png', thresh_image)
	# 	cv2.imwrite(name + '3.png', blur_img)
	# 	print('{0} 1: \t{1:,}\n{2} 2: \t{3:,}\n{4} 3: \t{5:,}'.format(name, val, name, val2, name, val3))
	
	return max([val, val2, val3])
	
#Initiliaze paths and variables
today = date.today()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Change to your installation path folder.
thresh = 127

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
os.system("")

gov_dead = 0
gov_kills_tier1 = 0
gov_kills_tier2 = 0
gov_kills_tier3 = 0
gov_kills_tier4 = 0
gov_kills_tier5 = 0
gov_rss_assistance = 0

image = cv2.imread('gov_info.png')

#Power and Killpoints
roi = (772, 230, 244, 38)
im_gov_id = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (890, 364, 170, 44)
im_gov_power = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (1114, 364, 222, 44)
im_gov_killpoints = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#1st image data
# ID
gov_id = image_to_string(im_gov_id, 'im_gov_id')
# power
gov_power = image_to_string(im_gov_power, 'im_gov_power')
# kill points
gov_killpoints = image_to_string(im_gov_killpoints, 'im_gov_killpoints')

#kills tier
image2 = cv2.imread('kills_tier.png')

roi = (861, 465, 215, 28) #tier 1
im_kills_tier1 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (861, 510, 215, 26) #tier 2
im_kills_tier2 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (861, 555, 215, 26) #tier 3
im_kills_tier3 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (861, 600, 215, 26) #tier 4
im_kills_tier4 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (861, 645, 215, 26) #tier 5
im_kills_tier5 = image2[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#2nd image data
gov_kills_tier1 = image_to_string(im_kills_tier1, 'im_kills_tier1')
gov_kills_tier2 = image_to_string(im_kills_tier2, 'im_kills_tier2')
gov_kills_tier3 = image_to_string(im_kills_tier3, 'im_kills_tier3')
gov_kills_tier4 = image_to_string(im_kills_tier4, 'im_kills_tier4')
gov_kills_tier5 = image_to_string(im_kills_tier5, 'im_kills_tier5')

#More info tab
image3 = cv2.imread('more_info.png')

roi = (1130, 443, 183, 40) #dead
im_dead = image3[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
roi = (1130, 668, 183, 40) #rss assistance
im_rss_assistance = image3[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#3rd image data
gov_dead = image_to_string(im_dead, 'im_dead')
gov_rss_assistance = image_to_string(im_rss_assistance, 'im_rss_assistance')

note = "ID: \t\t{0:,}\nPower: \t\t{1:,}\nKillpoints: \t{2:,}\nDead: \t\t{3:,}\nTier 1 kills: \t{4:,}\nTier 2 kills: \t{5:,}\nTier 3 kills: \t{6:,}\nTier 4 kills: \t{7:,}\nTier 5 kills: \t{8:,}\nRSS: \t\t{9:,}\n".format(gov_id,gov_power,gov_killpoints,gov_dead,gov_kills_tier1,gov_kills_tier2,gov_kills_tier3,gov_kills_tier4,gov_kills_tier5,gov_rss_assistance)
print(note)