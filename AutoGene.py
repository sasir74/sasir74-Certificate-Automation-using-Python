from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import csv

df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',40)
font1 = ImageFont.truetype("./MLSJN.TTF",60)
for index,j in df.iterrows():
    img = Image.open('temp.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(600,530),text='{}'.format(j['name']),fill=(24,19 ,0),font=font1)
    draw.text(xy=(620,780),text='OPERATIONAL INTERN',fill=(0,0,0),font=font)
    draw.text(xy=(185,930),text='SYNERGINA',fill=(0,0,0),font=font)
    draw.text(xy=(1250,930),text='28/03/2021',fill=(0,0,0),font=font) #Change-Daily
    img.save('pictures/{}.jpg'.format(j['name']))
