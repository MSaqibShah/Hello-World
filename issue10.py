import configparser

config = configparser.ConfigParser()
config.read('config.ini')
number = int(config['DEFAULT']['num'])

file = open('file1.txt','w')
str = "hello world"
size = number * 1024
size_count = 0
while size_count < size:
    file.write(str)
    size_count += len(str)
