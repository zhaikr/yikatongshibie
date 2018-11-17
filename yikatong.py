 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import cv2
import pytesseract
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import re

lujing = "/home/jackray/桌面/20181029_165827.jpg"
img = plt.imread(lujing)
#print(im)
#im2 = img.crop((200,100,200,100))
#im = img[2250:3200,1650:1900,:] #img[y,x,]
#plt.imshow(img)
#plt.show()
#将图片以数组的形式读入变量
#print (image_arr)
#print(img.shape) 
#shibie1 = pytesseract.image_to_string(im)
#print(shibie1)
x_list = []
y_list = []


def shibie(img):
    image_arr = np.array(img)
    y_fd,x_fd = img.shape[:2]
    for y in range(y_fd):
        for x in range(x_fd):
            pj = image_arr[y,x]
            a = pj[0]
            b = pj[1]
            c = pj[2]
            if a <= 1735 and a >= 158:
                if b <= 185 and b >= 175:
                    if c <= 105 and c >= 90:
                        y_list.append(y)
                        x_list.append(x)

def panduan(i,j,m,n,img):
    x_board = i-j
    y_board = m-n
    if x_board > y_board:
        img = Image.open(lujing)
        img = img.rotate(270, expand=True)
        img.save(lujing)
        img = plt.imread(lujing)
        x_list.clear
        y_list.clear
        shibie(img)
        xmax = max(x_list)
        xmin = min(x_list)
        ymax = max(y_list)
        ymin = min(y_list)
        return xmax,xmin,ymax,ymin

def xuehaoshibie(img):
    shibie(img)
    xmax = max(x_list)
    xmin = min(x_list)
    ymax = max(y_list)
    ymin = min(y_list)
    panduan(xmax,xmin,ymax,ymin,img)
    bili = (xmax-xmin)//365
    if bili == 0:
        bili = 1
    y_tezheng = (ymax+ymin)//2
    x_xhmax = xmin - 220*bili
    x_xhmin = xmin - 550*bili
    y_xhmin = ymin - 750*bili
    y_xhmax = y_tezheng
    im = img[y_xhmin:y_xhmax,x_xhmin:x_xhmax,:]
    shibiexuehao = pytesseract.image_to_string(im)
    b = re.compile('\d+')
    data = b.findall(shibiexuehao)[0]
    return data

data = xuehaoshibie(img)





