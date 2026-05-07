import pygame

pygame.init()  # Initialize Pygame
window = pygame.display.set_mode(size=(800, 600))  # Create a window
print("setup complete")

print("game loop started")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # End pygame
