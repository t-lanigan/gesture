import cv2
from gestures.gesture_recognizer import GestureRecognizer
from gestures.gesture_mappings import GESTURE_ACTIONS
from controllers.bluetooth_speaker import BluetoothSpeakerController
from controllers.philips_hue import PhilipsHueController

def main():
    """Main loop to recognize gestures and control devices."""
    cap = cv2.VideoCapture(0)
    gesture_recognizer = GestureRecognizer()

    # Initialize controllers
    speaker = BluetoothSpeakerController("00:11:22:33:44:55")  # Replace with actual address
    hue = PhilipsHueController()

    controllers = {
        "play_pause": speaker,
        "skip_track": speaker,
        "lights_on": hue,
        "lights_off": hue,
        "change_color": hue
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gesture = gesture_recognizer.recognize_gesture(frame)
        if gesture in GESTURE_ACTIONS:
            action = GESTURE_ACTIONS[gesture]
            if action in controllers:
                controllers[action].execute_action(action)

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()