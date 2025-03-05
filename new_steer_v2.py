import pygame
from math import sin, cos
from pylx16a.lx16a import *
import time

def set_speed(s):
    s = max(min(1000, s), -1000)
    
    #left side
    servo_28.motor_mode(s)
    servo_22.motor_mode(s)
    servo_27.motor_mode(s)
    #right side
    servo_21.motor_mode(-1*s)
    servo_20.motor_mode(-1*s)
    servo_23.motor_mode(-1*s)

def turn(t):
    # *** RANGE [0-80] (set of angles -> center +/- 40) ***
    #26 front-left, center at 40 (f)
    #24 front-right(X-X), center at 40 (f)
    #29 back-left(X-X),  center at 200 (bl)
    #25 back-right(X-X), center at 165 (br)

    t = max(min(40, t), -40)
    servo_24.move(f + t)
    servo_25.move(bl + t)
    servo_26.move(f + t)
    servo_29.move(br + t)




LX16A.initialize("COM12")
# Initialize pygame
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No controller connected!")

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller connected: {joystick.get_name()}")

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
    servo_24.set_angle_offset(-15)

    servo_25.servo_mode()
    #servo_25.set_angle_limits(0, 240)
    servo_25.set_angle_offset(30)

    servo_29.servo_mode()
    #servo_29.enable_torque()
    #servo_29.set_angle_limits(0, 240)
    servo_29.set_angle_offset(0)

    servo_26.servo_mode()
    #servo_26.set_angle_limits(0, 240)
    servo_26.set_angle_offset(30)

    # Normalizing Angles (facing forward)
    f = 40 
    bl = 200
    br = 165
    servo_24.move(f)
    servo_25.move(bl)
    servo_26.move(f)
    servo_29.move(br)

# Loop to read inputs
run = True
paused = False
servo_24.move(0) # Is this necessary? & Does it have to be here?

while run:
    # Check for button press
    for event in pygame.event.get():

    # Check for button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
            if event.button == 1:
                if paused:
                    print("Unpaused.")
                    paused = False
                else:
                    set_speed(0)
                    print("Paused.")
                    paused = True

    if not paused:
        left_y = joystick.get_axis(1)
        left_x = joystick.get_axis(0)
        turn(left_x * 40) if abs(left_x) > 0.2 else turn(0)
        set_speed(int(left_y * 1000)) if abs(left_y) > 0.2 else set_speed(0)
                    
pygame.quit()