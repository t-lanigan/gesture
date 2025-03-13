from phue import Bridge
import config  # Stores IP address of Hue Bridge

class PhilipsHueController:
    def __init__(self):
        self.bridge = Bridge(config.HUE_BRIDGE_IP)
        self.bridge.connect()

    def execute_action(self, action):
        if action == "lights_on":
            self.set_lights(True)
        elif action == "lights_off":
            self.set_lights(False)
        elif action == "change_color":
            self.change_color()

    def set_lights(self, state):
        print(f"Turning lights {'on' if state else 'off'}")
        self.bridge.set_light(1, 'on', state)

    def change_color(self):
        print("Changing light color")
        self.bridge.set_light(1, 'hue', 10000)  # Example hue value
