<div align="center">
  <img height="150" src="https://i.imgur.com/dI56gV3.png"  />
</div>
<div align="center">
  <img alt="GitHub License" src="https://img.shields.io/github/license/hizo9/sidek">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/hizo9/sidek">
</div>

<br>

## 🧾 SIDEK
*Sensor-Based Intelligent Detector for Waste Material in Ricefield Irrigation (Subak)*

A smart environmental monitoring system that combines real-time object detection, sensor data collection, and IoT-based alerting to detect and report waste accumulation levels at river barriers.

<br>

## 🔔 Notes
- This project uses [Grid Object Detection](https://github.com/hizo9/gridobjectdetection) as its core system for spatial analysis, dividing the scene into a 3x3 grid to monitor object occupancy in real time.
- Grid-based detection enables efficient tracking of spatial distribution, supporting automated responses like alerting when predefined thresholds are met.

<br>

## ✨ Features
- 🖥️ Real-time object detection using YOLO
- 🌐 Sensor integration: DHT22 and BH1750
- 💬 Telegram bot integration for alerts
- 📊 Dynamic 3x3 grid overlay for spatial analysis
- ⚠️ Threshold-based notification system

<br>

## 🔧 Requirements
- `opencv-python`
- `ultralytics`
- `adafruit-circuitpython-dht`
- `smbus`
- `requests`

<br>

## 📡 Hardware Used
- Raspberry Pi 5
- USB Webcam
- DHT22 Sensor
- BH1750 Sensor
- I2C Bus

<br>

## 🌍 Use Cases
- 🌊 Monitoring river waste barriers
- 🗑️ Tracking waste in waterways
- 🏙️ Smart city & environmental systems

<br>

## 📷 Project Overview
![screenshot1](https://i.imgur.com/eylMjqP.jpeg)
