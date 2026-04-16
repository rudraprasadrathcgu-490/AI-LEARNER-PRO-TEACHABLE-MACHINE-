# 🧠 AI Learner Pro

### 🚀 A Teachable Machine–Inspired AI Web App

AI Learner Pro is an interactive web-based application that allows users to train and test a custom image classification model using their own data. The system learns from user-uploaded images and predicts labels with confidence scoring, simulating real-world machine learning behavior.

---

## 🌐 Live Demo

🔗 https://ai-learner-pro-teachable-machine.onrender.com/

---

## ⚡ Features

* 🧠 **Custom AI Learning** — Train model with your own labeled images
* 🔍 **Smart Prediction System** — Classifies images with confidence scores
* ⚠️ **Unknown Detection** — Prevents incorrect predictions on unseen data
* 📊 **Dynamic Dataset Tracking** — View number of samples per label
* 🎯 **Low Confidence Handling** — Realistic AI uncertainty simulation
* 🎨 **Modern UI/UX** — Built with Tailwind CSS (Glassmorphism design)
* 📂 **Drag & Drop Upload** — Smooth and interactive user experience
* 🚀 **Deploy Ready** — Fully compatible with Render

---

## 🧠 How It Works

1. User uploads labeled images for training
2. Images are preprocessed (grayscale + resizing)
3. Histogram-based similarity is calculated
4. Model compares new image with stored dataset
5. Best match is selected using top-score logic
6. System outputs:

   * ✅ High Confidence Prediction
   * ⚠️ Low Confidence Prediction
   * ❌ Unknown (if not trained)

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, Tailwind CSS, JavaScript
* **Libraries:** NumPy, Pillow
* **Deployment:** Render

---

## 📁 Project Structure

```
ai-learner-pro/
│── app.py
│── learner.py
│── requirements.txt
│
├── data/                # Training dataset
├── static/
│   └── uploads/         # User uploaded images
│
└── templates/
    ├── index.html
    ├── train.html
    └── result.html
```


## 🎯 Use Cases

* Educational AI demonstrations
* Beginner-friendly ML projects
* Image classification experiments
* Portfolio project for internships

---

## 🧠 Key Highlights

* Implements **histogram-based image similarity**
* Uses **top-score selection instead of average** for better accuracy
* Includes **threshold-based unknown detection**
* Simulates **real-world ML uncertainty handling**

---

## 💡 Future Improvements

* 🎥 Webcam-based live prediction
* 🤖 Integration with real ML models (CNN)
* 📊 Accuracy graphs and analytics dashboard
* 🌍 Multi-class dataset visualization

---

## 👨‍💻 Author

Developed as part of an AI/ML internship project.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
