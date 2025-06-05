import cv2
import pyautogui
import threading
#from playsound import playsound  # Ensure playsound is installed: pip install playsound==1.2.2

from hand_tracker import HandTracker
from virtual_keyboard import VirtualKeyboard
from gesture_controller import GestureController
from key_mapper import KeyMapper
from utils import Debounce

def play_click_sound():
    threading.Thread(target=lambda: playsound('click.mp3'), daemon=True).start()

# Initialize camera
cap = cv2.VideoCapture(0)

# Set high resolution so the full keyboard fits
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Virtual Air Keyboard", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Virtual Air Keyboard", 1280, 720)

# Initialize components
tracker = HandTracker()
keyboard = VirtualKeyboard()
gesture = GestureController()
mapper = KeyMapper()
debounce = Debounce(delay=0.5)

# Track modifier keys
shift_active = False
caps_active = False

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    key_pressed = None

    # Get hand landmarks
    landmarks = tracker.find_hand_landmarks(frame)

    # Draw keyboard and get key positions
    key_positions = keyboard.draw_keyboard(frame)

    if landmarks:
        index_finger = mapper.get_index_finger_position(landmarks)

        if index_finger:
            x, y = index_finger
            cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)

            key = keyboard.get_key_at_position(x, y)

            if key:
                keyboard.highlight_key(frame, key_positions, key)

                if gesture.is_click(landmarks) and debounce.ready():
                    # Handle modifiers
                    if key == "Shift":
                        shift_active = not shift_active
                        mapper.set_shift(shift_active)

                    elif key == "Caps":
                        caps_active = not caps_active
                        mapper.toggle_caps_lock()

                    else:
                        # Set modifiers
                        mapper.set_shift(shift_active)
                        mapper.caps_lock = caps_active

                        # Press the key
                        mapper.trigger_key_press(key)
                        play_click_sound()

                        # Reset shift
                        if shift_active:
                            shift_active = False
                            mapper.set_shift(False)

    cv2.imshow("Virtual Air Keyboard", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
