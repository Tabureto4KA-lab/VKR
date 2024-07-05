import os, sys
from PIL import Image

path = "D:/ВКР (2)/dataset/all_cropped/"
dirs = os.listdir(path)

end_path = "D:/ВКР (2)/dataset/dataset/"

def rotate():
    i = 0
    for item in dirs:
        name = str(i)
        
        fullpath = os.path.join(path,item) 
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            
            if (i%4==0):
                im_rotate = im.rotate(90)
                im_rotate.save(end_path + name + '.bmp')
                print('saved')
                        
            elif (i%7==0):
                im_rotate = im.rotate(180)
                im_rotate.save(end_path + name + '.bmp')
                        
            elif (i%13==0):
                im_rotate = im.rotate(270)
                im_rotate.save(end_path + name + '.bmp')

            else:
                im.save(end_path + name + '.bmp')
            
            i=i+1

rotate()              
    