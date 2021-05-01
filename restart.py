# hours = int(input('Введите число часов для занятий:\n'))
#
# if hours >= 3:
#     print('Серёжа сегодня можёт поиграть!')
# else:
#     print('Занимайся дальше! Это тебе поможет')

#
# number = int(input('Введите число дней необходимых для появления привычки:\n'))
#
# for i in range(number):
#     if i == number - 1:
#         print('Поздравляем! У вас появилась полезная привычка')
#     else:
#         print(f'Нужно еще поработать над привычкой! Сегодня только лишь {i + 1} день')

# string = input('Введите строку:\n')
# print(f'Какая у меня длинная строка! В ней целых {len(string)} символов!')
# string_2 = 'Я молодец!'
# print(string_2[2:len(string_2) + 1])

# number = int(input('Введите количество дней, необходимых для получения привычки:\n'))
# while number != 0:
#     number -= 1
#     print(f'Вам надо еще поработать. Количество дней до приобретения привычки: {number}. Вы молодец!')
#     if number != 13:
#         continue
#     print('Continue работает! Ты Молодец!')
# print('Вы молодец. Вы получили полезную привычку! Так Держать!')

# a = [int(i) for i in input().split()]
# print(max(a))


# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(6))


# n = input('Введите целое число:\n')
#
# try:
#     n = int(n)
#     print('Преобразование прошло успешно!')
# except ValueError:
#     print('Что-то пошло не так. Невозможно преобразовать данную переменную в целочисленную переменную')
# finally:
#     print('Обработка исключений завершает свою работу')

# import pygame
# pygame.init()
#
# pygame.display.set_mode((1360, 720), pygame.RESIZABLE) # Создаем окно нашего приложения
# pygame.display.set_caption('Моя первая программа на PyGame!') # Заголовок
# pygame.display.set_icon(pygame.image.load('anya.bmp')) # Смена иконки окна программы
#
# clock = pygame.time.Clock()
# FPS = 60 # Неоходимое число кадров в секунду
#
# stop = True
# while stop:
#     for event in pygame.event.get(): # Обработка событий, происходящих в игре
#         if event.type == pygame.QUIT:
#             pygame.quit() # Завершение работы модуля PyGame
#             stop = False
#
#     clock.tick(FPS) # С помощью метода tick делаем ограничение по FPS (60 итераций цикла за секунду)
#
# print('Окно закрылось.\nВсё получится :-)')


# import pygame
# pygame.init()
#
# W, H = 600, 400
# GREEN = (0, 255, 0)
# BLUE = (0, 50, 255)
# RED = (255, 0, 0)
#
# sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # RESIZABLE - возможность менять размеры окна
# pygame.display.set_icon(pygame.image.load('anya.bmp'))
# pygame.display.set_caption('Графические примитивы')
# pygame.draw.rect(sc, GREEN, (300, 200, 150, 150), 7)  # Прямоугольник
# pygame.draw.line(sc, BLUE, (500, 350), (50, 100), 10)  # Линия
# pygame.draw.aaline(sc, GREEN, (300, 350), (50, 100))
# pygame.draw.polygon(sc, RED, [[30, 180], [100, 320], [200, 220], [300, 330]])
# pygame.display.update()  # "Переворачивает" экран на ту сторону, где были нарисованы примитивы
#
#
# stop = True
# FPS = 60
# clock = pygame.time.Clock()
#
# while stop:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             stop = False
#
#     clock.tick(FPS)

# Отклики программы от нажатий кнопок на клавиатуре

# import pygame
# pygame.init()
#
# FPS = 60
# W, H = 1360, 720
# sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
# pygame.display.set_icon(pygame.image.load('anya.bmp'))
# pygame.display.set_caption('Отклики программы от клавиатуры')
#
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
#
# clock = pygame.time.Clock()
#
# x = W//2  # Начальное положение прямоугольника на экране по оси X
# y = H//2  # Начальное положение прямоугольника на экране по оси Y
# speed = 5
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_UP]:
#         y -= speed
#     elif keys[pygame.K_DOWN]:
#         y += speed
#     elif keys[pygame.K_LEFT]:
#         x -= speed
#     elif keys[pygame.K_RIGHT]:
#         x += speed
#
#     sc.fill(WHITE)
#     pygame.draw.rect(sc, GREEN, (x, y, 50, 50))
#     pygame.display.update()
#
#     clock.tick(FPS)


# Отклики программы от нажатий кнопок на мышке


# import pygame
# pygame.init()
#
# W, H = 600, 400
#
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# WHITE = (255, 255, 255)
#
# FPS = 60
# clock = pygame.time.Clock()
#
# sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
# pygame.display.set_caption('Обработка событий от мыши')
# pygame.display.set_icon(pygame.image.load('anya.bmp'))
#
# sp = None
#
# sc.fill(WHITE)
# pygame.display.update()
# pygame.mouse.set_visible(False)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     pos = pygame.mouse.get_pos()
#     if pygame.mouse.get_focused():
#         pygame.draw.circle(sc, RED, pos, 8)
#
#     pressed = pygame.mouse.get_pressed()
#
#     if pressed[0]:
#
#         if sp is None:
#             sp = pos
#
#         width = pos[0] - sp[0]
#         height = pos[1] - sp[1]
#
#         sc.fill(WHITE)
#         pygame.draw.rect(sc, BLUE, (sp[0], sp[1], width, height), 8)
#     else:
#         sp = None
#     pygame.display.update()
#     clock.tick(FPS)


# Создание поверхностей Surface


import pygame

pygame.init()

W, H = 600, 400

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_icon(pygame.image.load('anya.bmp'))
pygame.display.set_caption('Создание поверхностей Surface')

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

surf = pygame.Surface((W, 200))
alpha = pygame.Surface((30, 40))

ax, ay = 0, 75
x, y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.fill(GREEN)
    alpha.fill(BLUE)
    surf.blit(alpha, (ax, ay))

    if ax < W:
        ax += 5
    else:
        ax = 0

    if x < H:
        y += 1
    else:
        y = 0

    sc.fill(WHITE)
    sc.blit(surf, (x, y))
    pygame.display.update()

    clock.tick(FPS)


def kek(a, b):
    return a + b


kek(5, 2)
