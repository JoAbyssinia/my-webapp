# 🖐️ Finger Tracking Emoji App

A Python web application that uses your webcam to track hand gestures and displays matching emojis in real-time!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-red.svg)

## ✨ Features

- 📷 Real-time webcam video streaming
- 🖐️ Hand landmark detection and visualization
- 🎯 Gesture recognition for multiple hand poses
- 😀 Instant emoji display matching your gestures
- 🎨 Modern, responsive web interface

## 🎮 Supported Gestures

| Gesture | Emoji | Description |
|---------|-------|-------------|
| Thumbs Up | 👍 | Thumb extended upward, other fingers closed |
| Thumbs Down | 👎 | Thumb extended downward, other fingers closed |
| Peace Sign | ✌️ | Index and middle fingers extended |
| Open Palm | 🖐️ | All five fingers extended |
| Fist | ✊ | All fingers closed |
| Pointing Up | 👆 | Only index finger extended |
| OK Sign | 👌 | Thumb and index forming a circle |
| Rock On | 🤘 | Index and pinky fingers extended |
| Pinky Up | 🤙 | Only pinky finger extended |

## 📁 Project Structure

```
gesture_recognition/
├── app.py                  # Main Flask application
├── gesture_recognition.py  # Gesture detection logic
├── templates/
│   └── index.html          # Web interface template
├── static/
│   └── style.css           # CSS styling
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam
- Modern web browser (Chrome, Firefox, Edge)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/JoAbyssinia/gesture_recognition.git
   cd gesture_recognition
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎬 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Allow camera access**
   When prompted, allow the browser to access your webcam

4. **Make gestures!**
   Show your hand to the camera and watch the emojis appear! 🎉

## 🛠️ Technologies Used

- **[Flask](https://flask.palletsprojects.com/)** - Web framework for Python
- **[OpenCV](https://opencv.org/)** - Computer vision library for video processing
- **[MediaPipe](https://mediapipe.dev/)** - Google's ML framework for hand tracking
- **[NumPy](https://numpy.org/)** - Numerical computing library

## 🔧 Troubleshooting

### Camera not working?

1. **Check permissions**: Ensure your browser has permission to access the webcam
2. **Close other apps**: Make sure no other application is using the camera
3. **Try a different browser**: Chrome or Firefox work best

### Gestures not recognized?

1. **Lighting**: Ensure good lighting conditions
2. **Background**: Use a plain background if possible
3. **Distance**: Keep your hand 1-2 feet from the camera
4. **Angle**: Face your palm towards the camera

### Installation issues?

If you encounter issues installing MediaPipe:
```bash
pip install --upgrade pip
pip install mediapipe --no-cache-dir
```

## 🌐 Browser Compatibility

| Browser | Status |
|---------|--------|
| Chrome | ✅ Fully supported |
| Firefox | ✅ Fully supported |
| Edge | ✅ Fully supported |
| Safari | ⚠️ May require permissions |

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author

**JoAbyssinia**

---

Made with ❤️ and Python 🐍
