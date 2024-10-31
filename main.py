import pygame  # Import the pygame library

# Initialize Pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600  # Width and height of the window
window = pygame.display.set_mode((width, height))  # Create the window

# Define colors
BLACK = (0, 0, 0)  # RGB for black
WHITE = (255, 255, 255)  # RGB for white
RED = (255, 0, 0)  # RGB for red

# Set up the square properties
square_size = 50  # Size of the square
x = width // 2  # Initial x position (center)
y = height // 2  # Initial y position (center)
x_speed = 5  # Speed in the x direction
y_speed = 5  # Speed in the y direction
color = RED  # Initial color of the square

# Main game loop
running = True
while running:
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # If the window is closed
            running = False  # Exit the loop

    # Update square position
    x += x_speed
    y += y_speed

    # Check for collision with window edges
    if x < 0 or x > width - square_size:  # If the square hits the left or right edge
        x_speed = -x_speed  # Reverse the x direction
        color = (255, 255, 0) if color == RED else RED  # Change color on collision

    if y < 0 or y > height - square_size:  # If the square hits the top or bottom edge
        y_speed = -y_speed  # Reverse the y direction
        color = (0, 255, 0) if color == RED else RED  # Change color on collision

    # Fill the window with black
    window.fill(BLACK)
    
    # Draw the square
    pygame.draw.rect(window, color, (x, y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
