#game snake

import pygame
import random

#using SOLID principals

from abc import ABC, abstractmethod

#initialisation pygame
pygame.init()

#screen setting
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CELL_SIZE = 20

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#game settings
FPS = 3

head_original = pygame.image.load("head.png")
snake_head = pygame.transform.scale(head_original, (20, 20))

body_original = pygame.image.load("body.png")
snake_body = pygame.transform.scale(body_original, (20, 20))

tail_original = pygame.image.load("tail.png")
snake_tail = pygame.transform.scale(tail_original, (20, 20))

turn_original = pygame.image.load("turn.png")
snake_turn = pygame.transform.scale(turn_original, (20, 20))

HEAD_IMAGES = {
    "UP": pygame.transform.rotate(snake_head, 90),
    "DOWN": pygame.transform.rotate(snake_head, 270),
    "LEFT": pygame.transform.rotate(snake_head, 180),
    "RIGHT": snake_head
}

BODY_IMAGE = {
    "UP": pygame.transform.rotate(snake_body, 90),
    "DOWN": pygame.transform.rotate(snake_body, 270),
    "LEFT": pygame.transform.rotate(snake_body, 180),
    "RIGHT": snake_body
}

TAIL_IMAGES = {
    "UP": pygame.transform.rotate(snake_tail, 90),
    "DOWN": pygame.transform.rotate(snake_tail, 270),
    "LEFT": pygame.transform.rotate(snake_tail, 180),
    "RIGHT": snake_tail
}
#inwterface for objects
class Drawable(ABC):

    @abstractmethod
    def draw(self, screen):
        pass

class Snake(Drawable):

    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]  # Начальная позиция змейки с хвостом
        self.directions = ["RIGHT", "RIGHT", "RIGHT"]  # Направления для каждого сегмента
        self.grow = False

    def move(self):
        head = self.body[0]
        if self.directions[0] == "RIGHT":
            new_head = [head[0] + CELL_SIZE, head[1]]
        if self.directions[0] == "LEFT":
            new_head = [head[0] - CELL_SIZE, head[1]]
        if self.directions[0] == "UP":
            new_head = [head[0], head[1] - CELL_SIZE]
        if self.directions[0] == "DOWN":
            new_head = [head[0], head[1] + CELL_SIZE]
        self.body.insert(0, new_head)
        self.directions.insert(0, self.directions[0])
        if not self.grow:
            self.body.pop()
            self.directions.pop()
        else:
            self.grow = False

    def change_direction(self, direction):
        opposites = {"RIGHT": "LEFT", "LEFT": "RIGHT", "UP": "DOWN", "DOWN": "UP"}
        if direction != opposites[self.directions[0]]:
            self.directions[0] = direction

    def check_collisions(self):
        head = self.body[0]
        if (head[0] < 0
                or head[0] >= SCREEN_WIDTH
                or head[1] < 0
                or head[1] >= SCREEN_HEIGHT
        ):
            return True
        if head in self.body[1:]:
            return True
        return False

    def grow_snake(self):
        self.grow = True

    def _turn_angle(self, prev_segment, curr_segment, next_segment):

        direction = {
            "From_right": prev_segment[0] < curr_segment[0],
            "From_left": prev_segment[0] > curr_segment[0],
            "From_down": prev_segment[1] < curr_segment[1],
            "From_up": prev_segment[1] > curr_segment[1],
            "To_right": curr_segment[0] > next_segment[0],
            "To_left": curr_segment[0] < next_segment[0],
            "To_down": curr_segment[1] > next_segment[1],
            "To_up": curr_segment[1] < next_segment[1]
        }

        if direction["From_left"] and direction["To_down"]:
            return 180
        if direction["From_left"] and direction["To_up"]:
            return 90
        if direction["From_right"] and direction["To_up"]:
            return 0
        if direction["From_right"] and direction["To_down"]:
            return -90

        if direction["From_up"] and direction["To_right"]:
            return 0
        if direction["From_up"] and direction["To_left"]:
            return 90
        if direction["From_down"] and direction["To_left"]:
            return 180
        if direction["From_down"] and direction["To_right"]:
            return -90

        return 0

    def draw(self, screen):
       # screen.blit(pygame.transform.rotate(turn_original, 90), (20, 20))

        # Отрисовка головы с учетом направления
        head_image = HEAD_IMAGES[self.directions[0]]
        screen.blit(head_image, (self.body[0][0], self.body[0][1]))

        # Отрисовка тела змейки
        for i in range(1, len(self.body) - 1):
            prev_segment = self.body[i - 1]
            curr_segment = self.body[i]
            next_segment = self.body[i + 1]
            if prev_segment[0] != next_segment[0] and prev_segment[1] != next_segment[1]:
                angle = self._turn_angle(prev_segment, curr_segment, next_segment)
                screen.blit(pygame.transform.rotate(snake_turn, angle), (curr_segment[0], curr_segment[1]))
#                print(f"prev segment: {prev_segment}, curr segment: {curr_segment}, next segment: {next_segment}, angle: {angle}")
            else:
                body_image = BODY_IMAGE[self.directions[i]]
                screen.blit(body_image, (self.body[i][0], self.body[i][1]))

        # Отрисовка хвоста
        tail_image = TAIL_IMAGES[self.directions[-1]]
        screen.blit(tail_image, (self.body[-1][0], self.body[-1][1]))



class Food(Drawable):
    def __init__(self):
        self.position = [random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]

    def generate_food(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            new_position = [x, y]
            if new_position not in snake_body:
                self.position = new_position
                break

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()

        self.game_over = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                if event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def update(self):
        self.snake.move()
        if self.snake.check_collisions():
            self.game_over = True
            print("Game Over")

        if self.snake.body[0] == self.food.position:
            self.snake.grow_snake()
            self.food.generate_food(self.snake.body)

    def render(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.process_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
