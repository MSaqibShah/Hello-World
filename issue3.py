import configparser

config = configparser.ConfigParser()
config.read('config.ini')
number = int(config['DEFAULT']['num'])
for i in range(number):
    print("Hello World")