import evdev

# Function to normalize joystick values (-1 to 1)
def normalize(value, min_val=0, max_val=255):
    return (value - min_val) / (max_val - min_val) * 2 - 1

# Find the PS5 controller device
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
controller = None

for device in devices:
    if "Wireless Controller" in device.name:  # PS5 is recognized as "Wireless Controller"
        controller = evdev.InputDevice(device.path)
        print(f"Connected to {device.name} at {device.path}")
        break

if not controller:
    print("No controller found.")
    exit()

# Read joystick movements
for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        abs_event = evdev.categorize(event)

        # Normalize joystick values
        if abs_event.event.code in [evdev.ecodes.ABS_X, evdev.ecodes.ABS_Y,
                                    evdev.ecodes.ABS_RX, evdev.ecodes.ABS_RY]:
            normalized_value = normalize(abs_event.event.value, min_val=0, max_val=255)
            axis_name = {
                evdev.ecodes.ABS_X: "Left Stick X",
                evdev.ecodes.ABS_Y: "Left Stick Y",
                evdev.ecodes.ABS_RX: "Right Stick X",
                evdev.ecodes.ABS_RY: "Right Stick Y"
            }.get(abs_event.event.code, "Unknown Axis")

            print(f"{axis_name}: {normalized_value:.2f}")
