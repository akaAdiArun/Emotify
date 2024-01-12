# Emotify: Real-Time Facial Expression Recognition

## Overview
Emotify is an advanced AI project that leverages the power of YOLOv8 for real-time facial expression recognition. This project aims to accurately detect and interpret human facial emotions, using a dataset sourced from Roboflow Universe.

## Technology Stack
- **YOLOv8**: The latest iteration in the YOLO series of real-time object detectors, known for its exceptional accuracy and speed in object detection tasks.
- **Python**: The project's primary programming language.
- **Ultralytics and Roboflow Libraries**: For integrating YOLOv8 and managing the dataset.

## Repository Structure
- **Data**: Human facial expressions dataset from [Roboflow Universe](https://universe.roboflow.com/human-face-expression-recognition/human-face-expression).
- **Python Scripts**:
  - `download.py`: Script to download the dataset.
  - `test.py`: Main script for training and testing the model.
- **Best_Model Folder**: Contains the trained YOLOv8 model optimized for facial expression recognition.

## Model Configuration
- **Task**: Detect
- **Mode**: Train
- **Model File**: `yolov8s.pt`
- **Dataset Path**: `C:/Users/adith/OneDrive/Documents/Emotify/Human-Face-Expression-20/data.yaml`
- **Epochs**: 20
- **Additional Parameters**: Various parameters for fine-tuning the model, including batch size, image size, optimizer settings, etc.

## Features of YOLOv8
- **Anchor-Free Detection**: Predicts the center of objects, simplifying the detection process and improving speed.
- **Advanced Backbone and Neck Architectures**: Enhances feature extraction and detection performance.
- **Versatility**: Supports various tasks like object detection, instance segmentation, pose/keypoints detection, and classification.

## Performance
YOLOv8 is known for its state-of-the-art performance in object detection. It achieves high accuracy while maintaining an optimal balance between speed and precision, making it ideal for real-time applications like Emotify.

## Usage
To run Emotify, use the `test.py` script. This will initiate the training process based on the provided dataset and configuration. The trained model can then be used for real-time facial expression recognition.

## Contributions and Support
Emotify is an open-source project. Contributions, suggestions, and feedback are welcomed. For detailed documentation on YOLOv8 and its implementation, refer to the [Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com) and the comprehensive guide on [LearnOpenCV](https://learnopencv.com/yolov8-comprehensive-guide-to-state-of-the-art-object-detection/).

