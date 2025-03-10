import pygame
from math import sin, cos
from pylx16a.lx16a import *
import time

def control_motors(l, r):
    #print(f"Left Motors: {left_speed}, Right Motors: {right_speed}") 
    
    left_speed = max(min(1000, int(l)), -1000)
    right_speed = max(min(1000, -1 * int(r)), -1000)
    #left side
    servo_28.motor_mode(left_speed)
    servo_22.motor_mode(left_speed)
    servo_27.motor_mode(left_speed)

    #right side
    servo_21.motor_mode(right_speed)
    servo_20.motor_mode(right_speed)
    servo_23.motor_mode(right_speed)
    _speed = [left_speed, right_speed]
    return _speed


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

# Loop to read inputs
run = True
speed = [0,0]
base_speed = 0
while run:

    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
        #    break

        # Check for button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
            if event.button == 1:
                control_motors(0,0)
                run = False
                break

        
        if (event.type == pygame.JOYAXISMOTION):
            if abs(event.value) > 0.2:
                print(f"Axis {event.axis} moved to {event.value}")
                # Left Joystick
                # Axis 0 = y (negative up)
                # Axis 1 = x (negative left)
                flag = 0
                if event.axis == 0:
                    if abs(base_speed) < 1000:
                        base_speed = base_speed+(event.value*1000)
                        speed[0] = speed[1] = base_speed 
                        flag = 1
                elif event.axis == 1:
                    if event.value > 0: #right
                        speed[0] = base_speed+(event.value*1000)
                        speed[1] = base_speed-(event.value*1000)
                    else: #left
                        speed[0] = base_speed-(event.value*1000)
                        speed[1] = base_speed+(event.value*1000)
                    flag = 1
            else:
                speed = [0,0]
                flag = 1
            if(flag): 
                speed = control_motors(speed[0], speed[1])
                flag = 0
            time.sleep(0.01)
pygame.quit()
