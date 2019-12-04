#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:02:00 2019

@author: owner


#Q1
import statistics as st

x=[3,1.5,4.5,6.75,2.25,5.75,2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

'''
#OUT
3.7142857142857144
2.8769027134348115
3
3
3
3.0
2.25
1.8391990270833904
3.38265306122449
1.9865619978819116
3.9464285714285716
'''

#Q2

import random

print( random.random() )
print (random.randrange(10))
print (random.choice (['Ali', 'Khalid', 'Hussam']))
print (random.sample (range (1000), 10) )
print (random.choice('OrangeAcademy'))
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items)
print (random.randint(20, 30) )
print (random.randrange(1000, 2111, 5))
print (random.uniform(10000, 11000))
'''
#OUT
0.569794506188586
2
Hussam
[828, 169, 151, 929, 803, 805, 6, 135, 161, 671]
e
[4, 1, 2, 9, 8, 5]
22
1455
10011.107117757696
'''

#Q3
import math


print(math.pi) #3.141592653589793

#print (math.sin(30))
#print (math.cos(200))
#print (math.tan(180))
print(math.floor(10.8)) #10
print(math.ceil(10.8))  #11


#Q4

from PIL import Image,ImageFilter
from PIL import ImageDraw

im=Image.open("cat.jpeg")
im2=Image.open("cat2.jpeg").resize(im.size)
#im2.show()

#1
print(im.format, im.size, im.mode)
#im.show()

#2
imgflip=im.transpose(Image.FLIP_TOP_BOTTOM)
#imgflip.show()

#3
greyimage=im.convert('L')
#greyimage.show()

#4
crop=im.crop((0,0,50,50))
#crop.show()

#5
#draw=ImageDraw.Draw(im)
#draw.line((0,0)+im.size, fill=(255,255,255))
#draw.line((0,im.size[1],im.size[0],0), fill=(255,255,255))
#draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'yasmin',fill=(225,225,0))
#im.show()

#6
new=im.filter(ImageFilter.SHARPEN)
#new.show()

enh=im.filter(ImageFilter.EDGE_ENHANCE)
#enh.show()

find=im.filter(ImageFilter.FIND_EDGES)
#find.show()


smo=im.filter(ImageFilter.SMOOTH)
#smo.show()

#7
Image.blend(im,im2,0.5).save('blendimg.jpg'.format(0.5))
new=Image.open('blendimg.jpg')
#new.show()

#8
blu=im.filter(ImageFilter.BLUR)
#blu.show()

#9
size=(128,128)
im.thumbnail(size)
#im.show()

#10
imagerot=im.rotate(90)
#imagerot.show()

#11
mask=Image.open('mask.jpg')
mask=mask.resize(im.size)
Image.composite(im,im2,mask).save('maskimg.jpg')
imagMask=Image.open('maskimg.jpg')
imagMask.show()


"""











