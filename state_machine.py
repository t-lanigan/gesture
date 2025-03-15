import cv2
import mediapipe as mp
from enum import Enum

class LightState(Enum):
    IDLE = 0
    ENGAGED = 1
    MEASURING = 2
    ADJUSTING = 3

class GestureLightController:
    def __init__(self):
        self.state = LightState.IDLE
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.brightness = 0.5  # Initial brightness (range 0 to 1)

    def process_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Get landmarks
                thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]

                # Determine if hand is open or closed
                hand_open = all(f.y < index_tip.y for f in [middle_tip, ring_tip, pinky_tip])
                hand_closed = all(f.y > index_tip.y for f in [middle_tip, ring_tip, pinky_tip])

                # State transitions
                if self.state == LightState.IDLE and hand_open:
                    self.state = LightState.ENGAGED

                elif self.state == LightState.ENGAGED and hand_closed:
                    self.state = LightState.MEASURING

                elif self.state == LightState.MEASURING and hand_open:
                    self.state = LightState.ADJUSTING

                elif self.state == LightState.ADJUSTING:
                    self.adjust_brightness(index_tip.y)
                    if hand_closed:
                        self.state = LightState.IDLE  # Reset state after adjustment

        cv2.putText(frame, f"State: {self.state.name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        return frame

    def adjust_brightness(self, hand_y_position):
        self.brightness = max(0, min(1, 1 - hand_y_position))  # Invert for natural control
        print(f"Brightness: {self.brightness:.2f}")  # Replace with actual light control logic

def main():
    cap = cv2.VideoCapture(0)
    controller = GestureLightController()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = controller.process_frame(frame)
        cv2.imshow('Gesture Light Control', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
