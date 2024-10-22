import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Lines Intersection")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Количество отрезков
num_segments = 10000  # Настраиваемое количество отрезков

# Расстояние между горизонтальными линиями
num_lines = 3
line_spacing = height // (num_lines + 1)
segment_length = line_spacing / 2

# Функция для отрисовки горизонтальных линий
def draw_lines():
    for i in range(1, num_lines + 1):
        pygame.draw.line(screen, BLACK, (0, i * line_spacing), (width, i * line_spacing), 2)

# Функция для генерации случайного отрезка
def generate_random_segment():
    # Случайные координаты центра отрезка
    x_center = random.uniform(segment_length / 2, width - segment_length / 2)
    y_center = random.uniform(segment_length / 2, height - segment_length / 2)
    
    # Случайный угол поворота отрезка
    angle = random.uniform(0, math.pi)
    
    # Вычисление координат концов отрезка
    x_offset = math.cos(angle) * segment_length / 2
    y_offset = math.sin(angle) * segment_length / 2
    x1, y1 = x_center - x_offset, y_center - y_offset
    x2, y2 = x_center + x_offset, y_center + y_offset
    
    return (x1, y1, x2, y2)

# Функция для проверки пересечения отрезка с горизонтальными линиями
def check_intersection(x1, y1, x2, y2):
    intersections = 0
    for i in range(1, num_lines + 1):
        line_y = i * line_spacing
        if (y1 < line_y < y2) or (y2 < line_y < y1):
            intersections += 1
    return intersections

# Основной цикл программы
def main():
    running = True
    clock = pygame.time.Clock()
    
    # Хранение всех отрезков
    segments = []
    intersecting_segments = 0
    
    # Генерация отрезков
    for _ in range(num_segments):
        x1, y1, x2, y2 = generate_random_segment()
        segments.append((x1, y1, x2, y2))
        if check_intersection(x1, y1, x2, y2) > 0:
            intersecting_segments += 1
    
    # Вычисление результата
    if intersecting_segments > 0:
        result = num_segments / intersecting_segments
    else:
        result = "No intersections"
    
    # Отображение результата в консоли
    print(f"Total segments: {num_segments}")
    print(f"Intersecting segments: {intersecting_segments}")
    print(f"Result: {result}")
    
    while running:
        screen.fill(WHITE)
        
        # Отрисовка горизонтальных линий
        draw_lines()
        
        # Отрисовка отрезков
        for x1, y1, x2, y2 in segments:
            pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 2)
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
