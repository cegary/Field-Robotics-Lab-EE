from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("COM12")

try:
    #Motors
    servo_20 = LX16A(20)
    servo_21 = LX16A(21)
    servo_22 = LX16A(22)
    servo_23 = LX16A(23)
    servo_27 = LX16A(27)
    servo_28 = LX16A(28)

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
    #servo_25.set_angle_offset(19)

    servo_29.servo_mode()
    servo_29.enable_torque()
    #servo_29.set_angle_limits(0, 240)
    servo_29.set_angle_offset(30)

    servo_26.servo_mode()
    #servo_26.set_angle_limits(0, 240)
    #servo_26.set_angle_offset(20)
    

    servo_28.motor_mode(400)
    servo_21.motor_mode(400)
    servo_20.motor_mode(400)
    servo_23.motor_mode(400)
    servo_22.motor_mode(400)
    servo_27.motor_mode(400)
    #servo29.set_angle_limits(0, 240)
    #servo_29.move(0)
    time.sleep(5)
    servo_28.motor_mode(0)
    servo_21.motor_mode(0)
    servo_20.motor_mode(0)
    servo_23.motor_mode(0)
    servo_22.motor_mode(0)
    servo_27.motor_mode(0)
    
    


except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
