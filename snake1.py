
from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Colors
background = (0, 0, 0)  # Black
snake_color = (0, 255, 0)  # Green
food_color = (255, 0, 0)  # Red

# Game settings
width = 8
height = 8
initial_length = 3

# Initialize snake
snake = [(3, 3), (3, 4), (3, 5)]
direction = 'left'
food = (random.randint(0, width-1), random.randint(0, height-1))

def draw_snake():
    sense.clear()
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], snake_color)
    sense.set_pixel(food[0], food[1], food_color)

def move_snake():
    global food  # Declare food as global here
    head_x, head_y = snake[0]
    if direction == 'up':
        head_y = (head_y - 1) % height
    elif direction == 'down':
        head_y = (head_y + 1) % height
    elif direction == 'left':
        head_x = (head_x - 1) % width
    elif direction == 'right':
        head_x = (head_x + 1) % width

    new_head = (head_x, head_y)
    if new_head in snake:
        return False  # Game over

    snake.insert(0, new_head)
    if new_head == food:
        # Increase length and place new food
        food = (random.randint(0, width-1), random.randint(0, height-1))
    else:
        snake.pop()
    return True

def update_direction(event):
    global direction
    if event.action == 'pressed':
        if event.direction == 'up' and direction != 'down':
            direction = 'up'
        elif event.direction == 'down' and direction != 'up':
            direction = 'down'
        elif event.direction == 'left' and direction != 'right':
            direction = 'left'
        elif event.direction == 'right' and direction != 'left':
            direction = 'right'

sense.stick.direction_up = update_direction
sense.stick.direction_down = update_direction
sense.stick.direction_left = update_direction
sense.stick.direction_right = update_direction

while True:
    draw_snake()
    if not move_snake():
        sense.show_message("Game Over", text_colour=(255, 0, 0))
        break
    sleep(0.5)
