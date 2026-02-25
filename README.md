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

## Learning Outcomes

Real-time video processing using OpenCV

Hand landmark detection with MediaPipe

Modular Python project design

Gesture logic using geometric distance calculations

Future Improvements

Dynamic thresholding based on hand size

Gesture classification (peace, fist, open palm)

Multi-hand support


Commit the change.

---

## 3. Add `.gitignore` if not already done

Create `.gitignore` (locally or on GitHub) with:


venv/
pycache/
*.pyc
.env


This signals you know basic repo hygiene.

---

## 4. Add repo description & tags (small but visible)

On GitHub → **About** section:

**Description**
> Real-time hand gesture recognition using OpenCV and MediaPipe

**Topics**

python
opencv
mediapipe
computer-vision
hand-tracking


This improves searchability.

---

## 5. Optional but powerful: demo GIF

If you want it to stand out:

1. Record 5–8 seconds (OBS / Xbox Game Bar)
2. Convert to GIF
3. Upload to `assets/demo.gif`
4. Add to top of README:



People trust visuals more than text.

---

## 6. Final commit message style (important habit)

Examples of **good** messages:
- `Add project README with usage instructions`
- `Add gitignore to exclude virtual environment`
- `Update requirements for reproducible setup`

Avoid:
- `final`
- `updated`
- `done`

---

## 7. How this now reads to a reviewer

Without you saying anything, your repo communicates:
- modular thinking
- dependency awareness
- version control literacy
- computer vision fundamentals

That’s exactly what an early engineering project should say.

---

You are officially past “student repo” territory.

Next logical moves *after* this (only if you want):
- link this repo on your CV
- write a short LinkedIn post
- add one more CV-focused feature

But as of now — **your GitHub part is complete**.
pip install -r requirements.txt
python NumberIdentifier.py
