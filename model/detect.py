import cv2
import torch
from pathlib import Path
from ultralytics import YOLO

model_path = Path(__file__).parent / 'yolov8n.pt'  # Adjust the model file name/path accordingly
print(model_path)
# Load the YOLOv8 model
model = YOLO(model_path)

def detect_faces(video_path):
    print(video_path)
    video = video_path.split('\\')[1]
    output_path = f'outputs/{video}_face_detected.mp4'
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for det in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, det[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    return output_path
