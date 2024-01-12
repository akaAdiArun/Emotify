import os
from ultralytics import YOLO
from roboflow import Roboflow

print("----- Training -----")
#Change the location of the data here
os.system("yolo task=detect mode=train model=yolov8s.pt data=C:/Users/adith/OneDrive/Documents/Emotify/Human-Face-Expression-20/data.yaml epochs=10 imgsz=800 plots=True batch=-1 device=0") 
