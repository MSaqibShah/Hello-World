import configparser
import os
import random

#FUNCTION TO GENERATES COLOURS (R,G,B)
def col_gen():
    col = random.randint(0,16777215)
    hex_num =str(hex(col))
    hex_col = hex_num[2:]
    hexa = '#'+ hex_col
    return hexa
#GETTING VARIAVBLE FROM CONFIG FILE
config = configparser.ConfigParser()
config.read("config.ini")
n = int(config['DEFAULT']['num'])


#GENERATING A STRING WITH "HELLO WORLD" n TIMES
stri = ""
for i in range(n):
    col = col_gen()
    stri = stri + '<p style = "color:'+ col + ';">Hello World</p>'


#CREATING THE HTML PAGE
file = open('HelloWorldO.html','w')

str1 = """
<HTML>
<head>
<title> HELLO WORLD </title>
</head>
<BODY>""" +stri+"""</BODY>
</HTML>
"""
file.write(str1)
file.close()
os.startfile('HelloWorldO.html')
