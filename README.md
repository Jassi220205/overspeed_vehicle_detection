# Overspeed Vehicle Detection System

An AI-based traffic monitoring system that detects vehicles from surveillance
videos, tracks them, estimates their speed, and identifies overspeeding
vehicles using deep learning and computer vision.

The project also includes a web-based interface that allows users to upload
traffic videos and initiate automated vehicle detection and speed analysis.

---

## Project Overview

The Overspeed Vehicle Detection System is designed to automate vehicle
monitoring from traffic surveillance footage.

The system:

- Detects vehicles in traffic videos
- Tracks detected vehicles using unique IDs
- Estimates vehicle speed from frame-based movement
- Identifies vehicles exceeding the configured speed threshold
- Generates overspeed alerts
- Provides a web interface for video upload and processing
- Produces processed detection results

---

## Objectives

- Automate vehicle detection from traffic surveillance videos
- Monitor vehicle movement across video frames
- Estimate the speed of detected vehicles
- Identify overspeeding vehicles
- Provide a simple web interface for video processing
- Demonstrate the integration of AI/computer vision with web technologies

---

## Tech Stack

### AI / Computer Vision
- Python
- YOLOv8 Nano
- OpenCV
- PyTorch
- NumPy

### Web Technologies
- HTML
- CSS
- JavaScript
- React.js
- Flask

### Development Tools
- VS Code
- Git / GitHub

---

## System Workflow

```text
Traffic Video
      ↓
Video Upload
      ↓
Frame-by-Frame Processing
      ↓
Vehicle Detection using YOLOv8
      ↓
Vehicle Tracking
      ↓
Speed Estimation
      ↓
Speed Threshold Comparison
      ↓
Overspeed Detection
      ↓
Detection Results / Output
