# 🖐️🎨 AI Virtual Painter

Welcome to **AI Virtual Painter** – a fun, interactive application that turns your webcam into a real-time drawing canvas using hand gesture recognition! Powered by OpenCV, MediaPipe, and Python, this project allows you to draw or erase on your screen with just your fingers, without touching any physical surface. Perfect for creative experiments, educational demos, or just having fun.

---

## ✨ Features

- **Hand Gesture Recognition:** Detects and tracks your hand movements in real-time.
- **Drawing Mode:** Draw with your index finger simply by raising it!
- **Eraser Mode:** Use a special gesture to erase parts of your drawing.
- **Live FPS Display:** See how smoothly your system processes video frames.
- **Easy Controls:** Start drawing or erasing just by changing your hand gestures.

---

## 📦 Requirements

- Python 3.7+
- [OpenCV](https://opencv.org/) (`cv2`)
- [MediaPipe](https://google.github.io/mediapipe/)
- [NumPy](https://numpy.org/)

Install dependencies using:

```shell script
pip install opencv-python mediapipe numpy
```


---

## 🚀 Getting Started

1. **Clone this repository**  
```shell script
git clone https://github.com/<your-username>/ai-virtual-painter.git
   cd ai-virtual-painter
```

2. **Run the main program**  
```shell script
python main.py
```

3. **Enjoy drawing with your hand!**

---

## 🕹 Controls & Usage

- **Index finger up:** Enter drawing mode and start painting.
- **Index + middle finger up:** Enter eraser mode.
- **Other gestures:** Pause drawing, reset starting position, or switch modes.

**Exit:** Press `q` to quit the application window.

---


## 👏 Acknowledgments

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) — For robust real-time hand tracking.
- [OpenCV](https://opencv.org/) — For powerful computer vision tools.
- Contributors and the open source community.

---

## 📄 License

This project is licensed under the MIT License.

---

**Happy painting with AI! 🖼️✨**  
If you enjoy the project, please consider ⭐️ starring the repo!
