# ASCII Converter

![ASCII Convert Image Example](https://user-cdn.hackclub-assets.com/01a02ead-31f6-76cb-b161-9d64340632ba/2026-08-23_16-41-38.png)

ASCII Converter is simple image to ASCII converter. It works by first converting the image to grayscale, then converting the scale of how dark the image is to a 1-7 scale which is then used by the program to choose which character to use. It is printed line by line in a nested for loop.

The terminal text is coloured using ANSI espace codes, which are written as ```\033[38;2;R;G;Bm``` where you can use the values of an RGB code i.e. ```\033[38;2;255;255;255m``` for an RGB code of ```[255,255,255]```.

## How I Made It

I used the PIL (Python Image Library) to first open the coloured version of the image using ```.open()``` and resizing the image to fit the screen by using the image ratio. The width is set to 50 characters at all times, only the height changes so it doesn't cut off and you can't see the entire image. 

The image is converted to grayscale in which the process I described in the introductory paragraph occurs. During the nested for loop, while the program is looping through all the pixels, the code uses ```greyimg.getpixel((x,y))``` to determine character to use and ```img.getpixel((x,y))``` to determine colour.

## Installation

You can install the executable at <a href='https://dsochamp.github.io/ImgTrace'>https://dsochamp.github.io/ImgTrace</a>. You can upload any image you like by entering its file location on your device or you can test it out using the test image which can be reffered to as just ```image.png```.
