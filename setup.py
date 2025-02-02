from math import sin, cos
from pylx16a.lx16a import *
import time
l = []
r = []
def move(speed):
    # motor speed range [-1000:1000]
    if speed > 1000:
        speed = 1000
    elif speed < -1000:
        speed = -1000
    global l, r
    for i in range(3):
        l[i].motor_mode(speed)
        r[i].motor_mode(-1*speed)

def init():
    try:
        LX16A.initialize("COM12")
        #Motors
        servo_20 = LX16A(20) # front right
        servo_21 = LX16A(21) # mid right
        servo_23 = LX16A(23) # back right
        servo_27 = LX16A(27) # front left
        servo_22 = LX16A(22) # mid left
        servo_28 = LX16A(28) # back left 

        #Servos
        servo_24 = LX16A(24) # front right
        servo_25 = LX16A(25) # back right 
        servo_26 = LX16A(26) # front left
        servo_29 = LX16A(29) # back left

        servo_24.servo_mode()
        servo_25.servo_mode()
        servo_29.servo_mode()
        servo_26.servo_mode()
       

        global r, l
        #directional = [servo_24, servo_25, servo_26, servo_29]
        l = [servo_27, servo_22, servo_28]
        r = [servo_20, servo_21, servo_23]
        motors = [l,r]
        for m in motors:
            m.enable_torque()

        
    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

def main():
    init()
    #CODE HERE#




if __name__=="__main__":
    main()
    


