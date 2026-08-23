from PIL import Image

img = Image.open(input('Which image would you like to open? '))

ratio = img.width / img.height

img = img.resize((int(img.width / (img.width / 50)),int(img.height / ((img.height * ratio) / 50))))

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
