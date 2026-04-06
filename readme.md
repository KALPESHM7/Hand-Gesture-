# 🖐️ Hand Gesture Browser Control using OpenCV & MediaPipe

## 🚀 Project Overview
This project is a real-time hand gesture recognition system that uses a webcam to detect finger gestures and perform browser automation tasks like opening websites.

It demonstrates the basics of **gesture-based human-computer interaction**.

---

## 💡 Features
- Real-time hand tracking using MediaPipe
- Finger counting with stability filtering
- Gesture-based website control
- Cooldown system to prevent repeated triggers

---

## 🎯 Gesture Mapping

| Fingers | Action |
|--------|--------|
| 1      | Open Google |
| 2      | Open Facebook |
| 3      | Open YouTube |
| 4      | Reset counter |

---

## 🛠️ Tech Stack
- Python
- OpenCV
- MediaPipe

---

## ▶️ How to Run

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv

## Activate Environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

## Install Dependencies
pip install -r requirements.txt

##  Run Project
python main.py
