# Face Detection in Video Files Using YOLOv8

## Project Overview
This project is a web-based application for detecting faces in video files using the YOLOv8 model. It is built with Flask and uses OpenCV for video processing.

## Features
- Upload video files through a web interface.
- Process videos to detect faces.
- Highlight faces with bounding boxes.
- Download the processed video.

## Installation

### Prerequisites
- Python 3.7+
- Flask
- OpenCV
- PyTorch

### Setup
1. Clone the repository:
2. Install dependencies:


## Usage
1. Run the Flask app:
2. Navigate to `http://localhost:5000` in your web browser.
3. Upload a video file and wait for the processing to complete.
4. Download the processed video.

## How It Works
- The Flask app provides a simple interface for uploading video files.
- Uploaded videos are processed using the YOLOv8 model to detect faces.
- Detected faces are highlighted with rectangles in the output video.
