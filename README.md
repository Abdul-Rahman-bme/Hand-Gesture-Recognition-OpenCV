# Hand Gesture Recognition using OpenCV & MediaPipe

A real-time hand tracking and finger-counting system built using OpenCV and MediaPipe.
Designed with a reusable hand tracking module that can be integrated into other
computer vision applications.

## Features
- Real-time hand landmark detection
- Finger state estimation (open / closed)
- Finger counting (0–5)
- FPS monitoring
- Modular and reusable design

## Tech Stack
- Python
- OpenCV
- MediaPipe
- NumPy

## Project Structure
- handTrackingModule.py  
  Reusable module for hand detection and landmark extraction

- NumberIdentifier.py  
  Application script for finger counting and visualization

## Setup & Run
```bash
pip install -r requirements.txt
python NumberIdentifier.py
