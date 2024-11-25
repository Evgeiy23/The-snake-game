import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размер экрана
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка на Python')

# Размер блока змейки
block_size = 10

# Скорость игры
clock = pygame.time.Clock()
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счёта
def our_score(score):
    value = score_font.render("Счёт: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Функция для отображения текста
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Основная функция игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Позиция еды
    foodx = round(random.randrange(0, dis_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - block_size) / 10.0) * 10.0

    # Основной игровой цикл
    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Вы проиграли! Нажмите C для продолжения или Q для выхода", red)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Если змейка касается стен или самой себя
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с телом змейки
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for block in snake_List:
            pygame.draw.rect(dis, yellow, [block[0], block[1], block_size, block_size])

        our_score(Length_of_snake - 1)

        pygame.display.update()

        # Если змейка съела еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
