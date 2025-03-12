# Gesture-Controlled Home Automation using MediaPipe

## Overview
This project uses [Google's MediaPipe](https://developers.google.com/mediapipe) for hand gesture recognition to control home devices such as a Bluetooth speaker and Philips Hue smart lights. By detecting predefined hand gestures, users can seamlessly interact with their smart home devices without physical contact.

## Features
- **Gesture Recognition**: Uses MediaPipe's Hand Tracking to recognize different hand gestures.
- **Bluetooth Speaker Control**: Adjust volume, play/pause, and skip tracks using hand gestures.
- **Philips Hue Light Control**: Turn lights on/off, change colors, and adjust brightness with simple gestures.
- **Customizable Gestures**: Modify or add new gestures for additional home automation devices.

## Requirements
- Python 3.7+
- OpenCV
- MediaPipe
- Bluetooth libraries (e.g., `pybluez` for Linux/macOS, `bleak` for Windows/macOS)
- `phue` library for controlling Philips Hue lights
- NumPy
- A webcam for gesture input

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mediapipe-gesture-home-automation.git
   cd mediapipe-gesture-home-automation

2. Install dependancies
```make install deps```

3. Connect to the Bluetooth speaker and Philips Hue bridge:

Ensure that your Bluetooth speaker is paired with your computer.
Find the IP address of your Philips Hue bridge and configure it with the phue library.


# License
This project is licensed under the MIT License. Feel free to modify and contribute!

# Acknowledgments
Google MediaPipe for hand tracking.
OpenCV for image processing.
Philips Hue API for smart lighting control.
PyBluez/Bleak for Bluetooth device interaction.