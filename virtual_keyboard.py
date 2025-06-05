import cv2
import numpy as np

class VirtualKeyboard:
    def __init__(self):
        self.keyboard_layout = [
            ['Esc', '1','2','3','4','5','6','7','8','9','0','-','=', 'Back'],
            ['Tab','Q','W','E','R','T','Y','U','I','O','P','[',']','\\'],
            ['Caps','A','S','D','F','G','H','J','K','L',';','\'','Enter'],
            ['Shift','Z','X','C','V','B','N','M',',','.','/','Shift'],
            ['Space']
        ]

        self.key_width = 60
        self.key_height = 60
        self.key_spacing = 10
        self.start_x = 50
        self.start_y = 50

        self.key_positions = []

    def draw_keyboard(self, frame):
        overlay = frame.copy()
        self.key_positions.clear()
        y = self.start_y

        for row in self.keyboard_layout:
            x = self.start_x
            for key in row:
                w = self.key_width
                if key in ['Back', 'Caps', 'Enter', 'Shift', 'Space', 'Tab']:
                    if key == 'Space':
                        w = self.key_width * 5 + self.key_spacing * 4
                    else:
                        w = self.key_width * 2 + self.key_spacing

                h = self.key_height

                if y + h > frame.shape[0] or x + w > frame.shape[1]:
                    continue  # Skip keys that would go outside the frame

                self._draw_glassmorphic_key(overlay, (x, y), (w, h))

                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.7 if key != 'Space' else 1.0
                thickness = 2
                text_size, _ = cv2.getTextSize(key, font, font_scale, thickness)
                text_x = x + (w - text_size[0]) // 2
                text_y = y + (h + text_size[1]) // 2
                cv2.putText(overlay, key, (text_x, text_y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

                self.key_positions.append((key, x, y, w, h))
                x += w + self.key_spacing
            y += self.key_height + self.key_spacing

        alpha = 0.6
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        return self.key_positions

    def _draw_glassmorphic_key(self, img, top_left, size):
        x, y = top_left
        w, h = size

        if y + h > img.shape[0] or x + w > img.shape[1]:
            return

        roi = img[y:y+h, x:x+w].copy()
        if roi.size == 0:
            return

        blur = cv2.GaussianBlur(roi, (15, 15), 0)
        overlay_color = (255, 255, 255)
        opacity = 0.25
        white_layer = np.full(roi.shape, overlay_color, dtype=np.uint8)
        blended = cv2.addWeighted(blur, 1 - opacity, white_layer, opacity, 0)

        # Draw rounded rectangle with transparency (simulate with mask)
        mask = np.zeros((h, w, 3), dtype=np.uint8)
        cv2.rectangle(mask, (0, 0), (w, h), (255, 255, 255), -1)
        mask = cv2.GaussianBlur(mask, (11, 11), 0)
        blended = cv2.addWeighted(blended, 0.95, mask, 0.05, 0)

        img[y:y+h, x:x+w] = blended
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 1)

    def get_key_at_position(self, x, y):
        for key, kx, ky, kw, kh in self.key_positions:
            if kx < x < kx + kw and ky < y < ky + kh:
                return key
        return None

    def highlight_key(self, frame, key_positions, key_name):
        for key, x, y, w, h in key_positions:
            if key == key_name:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                break
