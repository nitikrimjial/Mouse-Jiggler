import random
import pyautogui
import time

while True:
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Generate a random x and y coordinate
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse cursor to the random position
    pyautogui.moveTo(x, y)

    # Wait for a random interval before moving again
    interval = random.uniform(1, 5)
    time.sleep(interval)
