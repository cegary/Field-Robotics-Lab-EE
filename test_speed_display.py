import pygame
import sys
from math import sin, cos
import time


   
def print_st(s, t):
    s = max(min(1000, s), -1000)
    t = max(min(40, t), -40)
    sys.stdout.write('\r' + 'Speed: ' + s + '/1000     Turn Axis: ' + t)
    sys.stdout.flush()


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


# Loop to read inputs
run = True
paused = False

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
                    print("Paused.")
                    paused = True

    if not paused:
        left_y = joystick.get_axis(1)
        left_x = joystick.get_axis(0)
        if abs(left_x) > 0.2 or abs(left_y) > 0.2: print_st(int(left_y * 1000), left_x * 40)
                    
pygame.quit()