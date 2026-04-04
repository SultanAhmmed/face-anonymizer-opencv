# Face Anonymizer using OpenCV

## 🚀 Overview

This project is a real-time face anonymization tool built using OpenCV. It detects human faces from a webcam or video stream and applies different anonymization techniques such as blurring, pixelation, or masking to protect identity.

This is useful for:

* Privacy-focused applications
* Surveillance systems
* Dataset preprocessing
* Computer vision learning projects

---

## 🎯 Features

* Real-time face detection
* Anonymization modes:
  * Gaussian Blur
    
* Works with:

  * Webcam
  * Video files
  * Images
* Lightweight and beginner-friendly

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV
* NumPy

---

## 📂 Project Structure

```
face-anonymizer-opencv/
│── main.py
│── anonymizer.py
│── utils.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/face-anonymizer-opencv.git
cd face-anonymizer-opencv
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run with Webcam

```bash
python main.py
```

### Run with Video File

```bash
python main.py --video path/to/video.mp4
```

---

## 🧩 How It Works

1. Capture frames from webcam/video
2. Detect faces using OpenCV Haar Cascade or DNN
3. Extract face region (ROI)
4. Apply anonymization:

   * Blur → Gaussian smoothing
   * Pixelate → Resize + scale
   * Mask → Fill rectangle
5. Display processed frame

---

## 🔧 Example Modes

### Blur Mode

Applies Gaussian blur to hide identity.

### Pixelation Mode

Reduces resolution of face region.

### Mask Mode

Covers face with solid rectangle.

---

## 📸 Future Improvements

* Use deep learning face detectors (DNN / YOLO)
* Add face tracking for efficiency
* Export anonymized videos
* Integrate with RTSP streams (CCTV)
* Add GUI (Tkinter or Streamlit)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

MIT License

---

## 👤 Author Sultan Ahmmed

Your Name
