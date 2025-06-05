

---

````markdown
# 🧊 AirKeys – Virtual Air Keyboard with Hand Gestures

AirKeys is a futuristic touchless virtual keyboard that lets you type in mid-air using only your hand gestures and webcam. Designed with a beautiful **glassmorphic UI**, it mimics real typing behavior with **click sounds**, full key support, and intelligent gesture detection.



---

## ✨ Features

- 🖐️ **Touchless Typing** via real-time hand gesture recognition
- ✨ **Glassmorphic Keyboard UI** (translucent, frosted design)
- 🔊 **Auditory Feedback** (click sound on key press)
- ⌨️ Full **QWERTY Layout** with functional keys: Shift, Caps, Enter, Backspace, Tab, Esc
- 👆 **Pinch-to-Click** gesture detection (index + thumb)
- 🧠 **Debounce System** to prevent multiple unintended key presses
- 🔁 **Modifier Key Support** (Shift toggles for temporary caps, Caps Lock for persistent)

---

## 📽️ How It Works

AirKeys uses **MediaPipe** for real-time hand tracking and identifies your index fingertip. When you bring your **thumb and index finger together**, it registers as a click. The system overlays a translucent virtual keyboard on the live webcam feed, giving you real-time visual and interactive feedback.

---

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/airkeys.git
   cd airkeys
````

2. **Install required libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python main.py
   ```

---

## 📦 Requirements

* `opencv-python`
* `mediapipe`
* `pyautogui`
* `numpy`
* `playsound` *(or pygame if you want cross-platform audio)*

You can install them all with:

```bash
pip install opencv-python mediapipe pyautogui numpy playsound
```

---

## 🔊 Optional: Click Sound

Place a `click.mp3` file in your root project directory. This sound will play each time a key is clicked.

---

## 🎮 Controls

* **Hover** your index finger over a key to preview
* **Pinch your thumb and index finger** to "click"
* **Toggle** Shift or Caps for uppercase
* Press **`q`** to exit the virtual keyboard

---

## 🧑‍💻 Developer

**Suprakash Biswas**

> Created as an innovative prototype combining hand tracking and user experience.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## ⭐ Contribute

If you liked **AirKeys**, consider ⭐ starring the repo and sharing your feedback. Contributions, feature ideas, or PRs are welcome!

```


```
