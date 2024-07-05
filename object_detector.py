from ultralytics import YOLO
from PIL import Image
import os.path, sys

path = "C:/programming/yolo8_test/VKR/Train"
directory = os.listdir(path)

def detect_defects(path):
    model = YOLO("C:/programming/yolo8_test/VKR/best.pt")
    for i in range(len(directory)-1):
        p = path + "/" + directory[i]
        model.predict(p, show=False, save=False)
        pic = model.predict(p, show=False, save=False)
        image = Image.open(pic)
        image.show()

detect_defects(path)