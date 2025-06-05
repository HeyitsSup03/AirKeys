import math

class GestureController:
    def __init__(self, click_threshold=40):
        self.click_threshold = click_threshold  # Pixels

    def is_click(self, landmarks):
        """
        Returns True if thumb and index finger tips are close enough to register a 'click'
        """
        if len(landmarks) < 9:
            return False

        # Index tip (8), Thumb tip (4)
        x_thumb, y_thumb = landmarks[4]
        x_index, y_index = landmarks[8]

        distance = math.hypot(x_index - x_thumb, y_index - y_thumb)
        return distance < self.click_threshold
