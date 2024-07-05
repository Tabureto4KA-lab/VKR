from PIL import Image
import os.path, sys

path = "D:/ВКР (2)/dataset/8/"
dirs = os.listdir(path)

def crop():
    i = 0
    for item in dirs:
        name = '7' + str(i)
        i+=1
        fullpath = os.path.join(path,item)         
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            x=945
            y=1104
            d=900
            imCrop = im.crop((x, y, x+d, y+d))
            imCrop.save("D:/ВКР (2)/dataset/7_cropped/" + name+'.bmp')
crop()