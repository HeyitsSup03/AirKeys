import pyautogui

class KeyMapper:
    def __init__(self):
        self.caps_lock = False
        self.shift = False

    def get_index_finger_position(self, landmarks):
        if len(landmarks) >= 9:
            return landmarks[8]  # Index finger tip
        return None

    def toggle_caps_lock(self):
        self.caps_lock = not self.caps_lock

    def set_shift(self, state: bool):
        self.shift = state

    def trigger_key_press(self, key):
        special_keys = {
            'Space': 'space',
            'Back': 'backspace',
            'Enter': 'enter',
            'Tab': 'tab',
            'Esc': 'esc'
        }

        # Handle Caps Lock and Shift toggle keys outside this function in main loop

        if key in special_keys:
            pyautogui.press(special_keys[key])
        else:
            # Decide uppercase or lowercase based on shift/capslock
            if (self.caps_lock and not self.shift) or (not self.caps_lock and self.shift):
                pyautogui.write(key.upper())
            else:
                pyautogui.write(key.lower())
