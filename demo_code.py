from math import sin, cos
from pylx16a.lx16a import *
import time
import evdev

def normalize(value, min_val=0, max_val=255):
    return (value - min_val) / (max_val - min_val) * 2 - 1

# Function to control motor speeds (Replace with actual motor control logic)
def control_motors(left_speed, right_speed):
    print(f"Left Motors: {left_speed}, Right Motors: {right_speed}") 
    #left side
    servo_28.motor_mode(left_speed)
    servo_22.motor_mode(left_speed)
    servo_27.motor_mode(left_speed)

    #right side
    servo_21.motor_mode(right_speed)
    servo_20.motor_mode(right_speed)
    servo_23.motor_mode(right_speed)


LX16A.initialize("/dev/ttyUSB0")

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

try:
    #Motors
    servo_20 = LX16A(20)
    servo_20.enable_torque()

    servo_21 = LX16A(21)
    servo_21.enable_torque()

    servo_22 = LX16A(22)
    servo_22.enable_torque()

    servo_23 = LX16A(23)
    servo_23.enable_torque()

    servo_27 = LX16A(27)
    servo_27.enable_torque()

    servo_28 = LX16A(28)
    servo_28.enable_torque()

    #Servos
    servo_24 = LX16A(24)
    servo_25 = LX16A(25)
    servo_26 = LX16A(26)
    servo_29 = LX16A(29)

    servo_24.servo_mode()
    #servo_24.set_angle_limits(0, 240)
    #servo24.set_angle_offset(-20) :needs fixing

    servo_25.servo_mode()
    #servo_25.set_angle_limits(0, 240)
    #servo_25.set_angle_offset(15)

    servo_29.servo_mode()
    #servo_29.enable_torque()
    #servo_29.set_angle_limits(0, 240)
    #servo_29.set_angle_offset(0)

    servo_26.servo_mode()
    #servo_26.set_angle_limits(0, 240)
    #servo_26.set_angle_offset(29)
    
    left_x=0
    left_y=0
    for event in controller.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            abs_event = evdev.categorize(event)

            # Read Left Stick X (steering) and Y (forward/backward)
            
            if abs_event.event.code == evdev.ecodes.ABS_X:
                left_x = normalize(abs_event.event.value, min_val=0, max_val=255)  # Left Stick X
            elif abs_event.event.code == evdev.ecodes.ABS_Y:
                left_y = normalize(abs_event.event.value, min_val=0, max_val=255)  # Left Stick Y

                # Movement Logic
                if left_y < -0.3:  # Move forward
                    base_speed = abs(left_y) * 1000  # Scale speed (0 to 100)
                    
                    if left_x < -0.3:  # Turn Left
                        left_motor = base_speed * 0.4  # Reduce left speed
                        right_motor = base_speed  # Keep right motor full
                    elif left_x > 0.3:  # Turn Right
                        left_motor = base_speed  # Keep left motor full
                        right_motor = base_speed * 0.4  # Reduce right speed
                    else:  # Move straight
                        left_motor = base_speed
                        right_motor = base_speed

                else:  # Stop when neutral
                    left_motor = 0
                    right_motor = 0

                # Control motors
                control_motors(left_motor, right_motor)

            # Sleep for a short time to reduce CPU usage
            time.sleep(0.05)

    
    


except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
