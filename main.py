from PIL import Image
import matplotlib.pyplot as plot
import numpy

img = Image.open(input('Which image would you like to open? '))

scale = int(input('What would you like your scale down to be? e.g. 2 is for 50% scale down '))

img = img.resize((int(img.width / scale),int(img.height / scale)))

greyimg = img.convert('L')

characters = '0|/!@*^&±%$# '

line = ''

for y in range(greyimg.height):
    for x in range(greyimg.width):
        index = int(greyimg.getpixel((x,y)) / (255/len(characters) + 1))
        colours = img.getpixel((x,y))
        line += f"\033[38;2;{colours[0]};{colours[1]};{colours[2]}m{characters[index]} \033[m"
        line += ' '

    print(line)
    line = ''
    

img.show()
