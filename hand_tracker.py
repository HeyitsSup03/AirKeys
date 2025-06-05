import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_confidence=0.7):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hand_landmarks(self, frame):
        """
        Returns a list of (x, y) tuples of detected hand landmarks in pixel coordinates.
        Also draws the landmarks on the frame.
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        landmarks = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                h, w, _ = frame.shape
                for lm in hand_landmarks.landmark:
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

        return landmarks
