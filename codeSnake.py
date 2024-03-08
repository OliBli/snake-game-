import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# Setup for game
width, height = 600, 400
Rows,Colom = 10,10
Square_size = width// Colom

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_front = pygame.font.SysFont("Helvetica", 25)
score_front = pygame.font.SysFont("Helvetica", 25)

# Initialize high score
high_score = 0
previous_score = 0 

#Load high score from file
try:
    with open("high_score_txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass  

# Funktion for keeping score
def printScore(score, high_score):
    text = score_front.render("Score:" + str(score), True, orange)
    high_score_text = score_front.render("High Score:" + str(high_score), True, orange)
    game_display.blit(text, [0, 0])
    game_display.blit(high_score_text, [0, 25])

# Funktion for drawing the snake
def drawSnake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

# Funktion for running the game
def run_game():
    global high_score  

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixel = []
    snake_length = 1

    # Food
    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Game over message
        while game_close:
            game_display.fill(black)
            game_over_message = message_front.render("Game over", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            restar_game = message_front.render("Spacebar to restart", True, orange)
            game_display.blit(restar_game, [width / 3, height / 2 ])
            close_game = message_front.render("Return to close", True, orange)
            game_display.blit(close_game, [width / 3, height / 1.7 ] )
            printScore(snake_length - 1, high_score)
            pygame.display.update()
            # Closing game or continue 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        with open("high_score_txt", "w") as file:
                            file.write(str(high_score))
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        run_game()
                if event.type == pygame.QUIT:
                    game_close = False
                    game_over = True
        # Game movment 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_d:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_s:
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_w:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixel.append([x, y])


        drawSnake(snake_size, snake_pixel)
        printScore(snake_length - 1, high_score)

        pygame.display.update()

        # Snake length incres 
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

            # Update high score
            if snake_length - 1 > high_score:
                high_score = snake_length - 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()