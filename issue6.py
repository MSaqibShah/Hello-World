import configparser
import os
#GETTING VARIAVBLE FROM CONFIG FILE
config = configparser.ConfigParser()
config.read("config.ini")
n = int(config['DEFAULT']['num'])


#GENERATING A STRING WITH "HELLO WORLD" n TIMES
str = ""
for i in range(n):
    str = str + "Hello World <br>"


#CREATING THE HTML PAGE
file = open('HelloWorldO.html','w')

str1 = """
<HTML>
<head>
<title> HELLO WORLD </title>
</head>
<BODY>""" +str+"""</BODY>
</HTML>
"""
file.write(str1)
file.close()
os.startfile('HelloWorldO.html')