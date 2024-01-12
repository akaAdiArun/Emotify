import torch
from ultralytics import YOLO


# Load the trained model
model = YOLO('best.pt')  # load a custom trained model

# Export the model
model.export(format='tflite')