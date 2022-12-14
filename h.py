import requests
from bs4 import BeautifulSoup
import openpyxl
import urllib.request
import wikipedia
import random
from PIL import Image
import matplotlib.pyplot as plt
import os
from skimage import io
import cv2


dataframe = openpyxl.load_workbook("book7000.xlsx")
 
# Define variable to read sheet
dataframe1 = dataframe.active
for row in range(0, dataframe1.max_row):
    for col in dataframe1.iter_cols(1, dataframe1.max_column):
        i=1
        j="1"
        print(col[row].value)
        word=(col[row].value)
        while(col[row].value !=""):
            params = {   
            "q": word,
            "tbm": "isch", 
            "content-type": "image/png",
            "dpi":1200,}

            html = requests.get("https://www.google.com/search?q", params=params)
            

            soup = BeautifulSoup(html.text, 'html.parser')

            img= soup.find("img")
            
            img=img.find_next('img')
           
            print(img['src'])  
            
           


            try:
                urllib.request.urlretrieve(img['src'], word+"_img_.png")
            except:
                e=open("error.txt","a")
                e.write(word+"\n")

                print("Error\n")


            i=i+1             
            if(i>=1):
                break
