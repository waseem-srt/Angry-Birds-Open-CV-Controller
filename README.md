# Gesture-Controlled Angry Birds 🎯  
_Control Angry Birds 2 with just your hand using Python & Computer Vision._

---

## **Overview**
Remember **Angry Birds 2**? Growing up, it was one of my favorite games.  
Now, I’ve combined it with **Python**, **OpenCV**, and **MediaPipe** to create a **gesture-controlled version** —  
**Fist** to pull the slingshot, **open hand** to release.  

This project is a fun blend of **childhood nostalgia** and **modern AI-powered interaction**.

---

## **Features**
- **Hand Gesture Recognition** – Detects fist & open palm in real-time.  
- **Mouse Emulation** – Moves the in-game cursor using your hand.  
- **Always-on-Top Preview** – See your camera feed even while playing in fullscreen.  
- **Smooth Movement** – Filtered hand tracking for precise control.  

---

## **Tech Stack**
- **Python** – Core language  
- **OpenCV** – Webcam input & image processing  
- **MediaPipe Hands** – 21-point hand landmark detection  
- **PyAutoGUI** – Mouse control (move, click, release)  
- **Win32 API** – Keep camera preview window always on top  
- **Virtual Environment (venv)** – Isolated Python environment  

---

## **How It Works**
1. **OpenCV** captures webcam feed.  
2. **MediaPipe** detects hand landmarks (21 points).  
3. **Gesture logic** determines:
   - **Fist** → Pull slingshot (mouseDown).  
   - **Open palm** → Release (mouseUp).  
4. **PyAutoGUI** moves the system mouse based on hand position.  
5. **Win32 API** keeps the camera feed window floating on top of Angry Birds.  

---

## **Setup & Installation**

### **1. Clone the repository**
```bash
git clone https://github.com/yourusername/gesture-angrybirds.git
cd gesture-angrybirds
