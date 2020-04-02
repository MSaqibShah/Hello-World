import os
file = open('HelloWorld1.html','w')

str = '''
<HTML>
<head>
<title> HELLO WORLD </title>
</head>
<BODY>
<H1>HELLO WORLD</H1>
</BODY>
</HTML>
'''
file.write(str)
file.close()
os.startfile('HelloWorld1.html')

