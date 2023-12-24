import pygame
import time
import random

pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white, red, green, black = (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)

# Snake properties
snake_block, snake_speed = 20, 15

# Initialize the snake
snake, snake_direction = [(width // 2, height // 2)], "RIGHT"

# Initialize the food
food_size, food_pos = 20, [random.randrange(1, (width // snake_block)) * snake_block,
                           random.randrange(1, (height // snake_block)) * snake_block]

# Score
score = 0

font = pygame.font.SysFont(None, 55)

def display_text(text, color, x, y):
    text_render = font.render(text, True, color)
    screen.blit(text_render, (x, y))

def reset_game():
    return [(width // 2, height // 2)], "RIGHT", [random.randrange(1, (width // snake_block)) * snake_block,
                                                   random.randrange(1, (height // snake_block)) * snake_block], 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_SPACE:
                snake, snake_direction, food_pos, score = reset_game()

    # Move the snake
    new_head = {
        "UP": (0, -snake_block),
        "DOWN": (0, snake_block),
        "LEFT": (-snake_block, 0),
        "RIGHT": (snake_block, 0)
    }[snake_direction]

    new_head = (snake[0][0] + new_head[0], snake[0][1] + new_head[1])

    # Check for collisions with walls or itself
    if any(coord < 0 or coord >= size for coord, size in zip(new_head, (width, height))) or new_head in snake[1:]:
        screen.fill(black)
        display_text("Game Over", red, width // 2 - 130, height // 2 - 30)
        display_text("Play Again (Space)", white, width // 2 - 170, height // 2 + 30)
        pygame.display.update()
        pygame.time.delay(2000)

        snake, snake_direction, food_pos, score = reset_game()

    snake.insert(0, new_head)

    # Check if snake eats the food
    if new_head[0] == food_pos[0] and new_head[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (width // snake_block)) * snake_block,
                    random.randrange(1, (height // snake_block)) * snake_block]
    else:
        snake.pop()

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, green, (*food_pos, food_size, food_size))

    for x, y in snake:
        pygame.draw.rect(screen, white, (x, y, snake_block, snake_block))

    display_text(f"Score: {score}", white, 10, 10)
    pygame.display.update()

    # Set the game speed
    pygame.time.Clock().tick(snake_speed)
