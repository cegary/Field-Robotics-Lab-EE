import pygame

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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")

        # Check for axis movement (e.g., analog stick)
        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")

pygame.quit()
