import pygame
import time
import random

pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake properties
snake_block = 20  # Change the size of each block in the snake
snake_speed = 15

# Initialize the snake
snake = [(width // 2, height // 2)]
snake_direction = "RIGHT"

# Initialize the food
food_size = 20  # Change the size of the food
food_pos = [random.randrange(1, (width // snake_block) - 1) * snake_block,
            random.randrange(1, (height // snake_block) - 1) * snake_block]

# Score
score = 0

font = pygame.font.SysFont(None, 55)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

def game_over_screen():
    game_over_text = font.render("Game Over", True, red)
    play_again_text = font.render("Play Again (Space)", True, white)

    game_over_x = width // 2 - game_over_text.get_width() // 2
    game_over_y = height // 2 - game_over_text.get_height() // 2 - 30

    play_again_x = width // 2 - play_again_text.get_width() // 2
    play_again_y = height // 2 - play_again_text.get_height() // 2 + 30

    screen.blit(game_over_text, (game_over_x, game_over_y))
    screen.blit(play_again_text, (play_again_x, play_again_y))

# Create a Clock object
clock = pygame.time.Clock()

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
                # Reset the game if the player presses Space
                snake = [(width // 2, height // 2)]
                snake_direction = "RIGHT"
                food_pos = [random.randrange(1, (width // snake_block) - 1) * snake_block,
                            random.randrange(1, (height // snake_block) - 1) * snake_block]
                score = 0

    # Move the snake
    new_head = (0, 0)
    if snake_direction == "UP":
        new_head = (snake[0][0], snake[0][1] - snake_block)
    elif snake_direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + snake_block)
    elif snake_direction == "LEFT":
        new_head = (snake[0][0] - snake_block, snake[0][1])
    elif snake_direction == "RIGHT":
        new_head = (snake[0][0] + snake_block, snake[0][1])

    # Check for collisions with walls or itself
    if (
        new_head[0] >= width
        or new_head[0] < 0
        or new_head[1] >= height
        or new_head[1] < 0
    ):
        screen.fill(black)
        game_over_screen()
        display_score(score)
        pygame.display.update()
        pygame.time.delay(2000)  # Delay for 2000 milliseconds (2 seconds)

        # Reset the game after delay
        snake = [(width // 2, height // 2)]
        snake_direction = "RIGHT"
        food_pos = [random.randrange(1, (width // snake_block) - 1) * snake_block,
                    random.randrange(1, (height // snake_block) - 1) * snake_block]
        score = 0

    for block in snake[1:]:
        if block == new_head:
            screen.fill(black)
            game_over_screen()
            display_score(score)
            pygame.display.update()
            pygame.time.delay(2000)  # Delay for 2000 milliseconds (2 seconds)

            # Reset the game after delay
            snake = [(width // 2, height // 2)]
            snake_direction = "RIGHT"
            food_pos = [random.randrange(1, (width // snake_block) - 1) * snake_block,
                        random.randrange(1, (height // snake_block) - 1) * snake_block]
            score = 0

    snake.insert(0, new_head)

    # Check if snake eats the food
    if new_head[0] == food_pos[0] and new_head[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (width // snake_block) - 1) * snake_block,
                    random.randrange(1, (height // snake_block) - 1) * snake_block]
    else:
        snake.pop()

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, green, [food_pos[0], food_pos[1], food_size, food_size])

    for segment in snake:
        pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

    display_score(score)
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)
