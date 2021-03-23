from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import csv

df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',90)
font1 = ImageFont.truetype("./MLSJN.TTF",110)
for index,j in df.iterrows():
    img = Image.open('as.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1500,1215),text='{}'.format(j['name']),fill=(24,19 ,0),font=font1)
    draw.text(xy=(890,1800),text='{}'.format(j['signature']),fill=(0,0,0),font=font)
    draw.text(xy=(2100,1800),text='22/03/2021',fill=(0,0,0),font=font) #Change-Daily
    img.save('pictures/{}.jpg'.format(j['name']))
