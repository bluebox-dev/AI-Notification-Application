# AI Notification Application

A real-time object detection system powered by YOLOv8 that identifies target objects via webcam or static images and sends instant notifications through Telegram. This application is specifically designed for coin detection and monitoring tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- **Real-time Object Detection**: Leverages YOLOv8 deep learning model for accurate object recognition
- **Multiple Input Sources**: Supports both webcam streaming and static image analysis
- **Telegram Integration**: Sends instant notifications with detection photos to your Telegram account
- **Configurable Thresholds**: Adjustable confidence levels and target classes for detection flexibility
- **Spam Prevention**: Built-in cooldown mechanism to avoid notification flooding
- **Visual Feedback**: Displays bounding boxes and confidence scores on detected objects

## Requirements

- Python 3.13 or higher
- OpenCV (cv2)
- Ultralytics YOLOv8
- NumPy
- Requests library
- PyTorch
- Telegram Bot Token and Chat ID

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd AI-Notification-Application
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individual packages:
   ```bash
   pip install ultralytics opencv-python requests torch torchvision
   ```

4. **Download the pre-trained model**:
   - Ensure the `best.pt` model file is in the project root directory
   - This file contains the trained YOLOv8 weights for object detection

## Configuration

Before running the application, configure the following parameters in the Python files:

### Telegram Setup
1. Create a Telegram bot using [BotFather](https://t.me/botfather)
2. Get your Chat ID by messaging your bot and using the `/start` command
3. Update the credentials in the code:
   ```python
   BOT_TOKEN = "your_bot_token_here"
   CHAT_ID = "your_chat_id_here"
   ```

### Detection Parameters
- `CONF_THRESHOLD`: Confidence threshold for detections (default: 0.5)
- `TARGET_CLASSES`: List of object classes to detect (default: coins "1", "5", "10")
- `COOLDOWN_SECONDS`: Minimum time between notifications (default: 10 seconds)

## Usage

### Real-time Detection (Webcam)

Run the real-time webcam detection:
```bash
python realtime.py
```

This will:
- Activate your default webcam
- Display a live preview window with detected objects highlighted
- Send Telegram notifications when target objects are detected
- Press 'q' to stop the application

### Static Image Detection

Analyze a single image file:
```bash
python detect.py
```

Ensure you have an `image-test.jpg` file in the project directory. The script will:
- Load and analyze the specified image
- Save detection results to `detected.jpg`
- Send the annotated image to Telegram if targets are found

## Project Structure

```
AI-Notification-Application/
├── best.pt                 # Pre-trained YOLOv8 model weights
├── detect.py              # Single image detection script
├── realtime.py            # Real-time webcam detection script
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies and versions
├── image-test.jpg         # Sample test image for detection
├── detected.jpg           # Output image with detection results
├── .git/                  # Git version control directory
└── env/                   # Virtual environment (optional)
```

## Technical Details

- **Detection Model**: YOLOv8 (You Only Look Once v8)
- **Computer Vision Framework**: OpenCV
- **Notification Service**: Telegram Bot API
- **Language**: Python 3.13

## Notes

- Ensure your webcam is properly connected and accessible before running `realtime.py`
- Keep your Telegram bot token and chat ID confidential
- Adjust confidence thresholds based on your specific use case and model accuracy
- The cooldown mechanism prevents excessive notifications while still maintaining responsiveness

## License

Please refer to the project's license file for usage terms and conditions.

---

**Developed**: February 2026