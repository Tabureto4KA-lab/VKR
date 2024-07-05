from ultralytics import YOLO

model = YOLO('yolov8m.pt')

def train(data, epochs):
    results = model.train(data, epochs)