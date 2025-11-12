import pygame


class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    STILL = (0, 0)


class Snake:
    BLOCK = 40
    SPEED = 4  # The lower the slower (1 is slowest, 10 is fastest)

    def __init__(self, x0, y0, images, color_snake=(0, 0, 0), size=BLOCK):
        self.length = 1
        self.head = [x0, y0]
        self.direction = Direction.STILL
        self.positions = []
        self.color_snake = color_snake
        self.images = images
        self.size = size

    @property
    def score(self):
        return max(0, self.length - 1)

    def draw(self, dis):
        for i, x in enumerate(self.positions):
            pygame.draw.rect(dis, self.color_snake, [x[0], x[1], self.size, self.size])
            if i == self.length - 1:
                # Rotate head image based on direction
                if self.direction == Direction.UP:
                    head_image = pygame.transform.rotate(self.images["head"], 90)
                elif self.direction == Direction.DOWN:
                    head_image = pygame.transform.rotate(self.images["head"], -90)
                elif self.direction == Direction.LEFT:
                    head_image = pygame.transform.rotate(self.images["head"], 180)
                else:
                    head_image = self.images["head"]
                dis.blit(head_image, (x[0], x[1]))
            elif i == 0:
                # Rotate tail image based on direction
                if self.length > 1:  # Ensure there is a tail to orient
                    next_pos = self.positions[1]
                    if x[0] < next_pos[0]:
                        tail_image = pygame.transform.rotate(self.images["tail"], 180)
                    elif x[0] > next_pos[0]:
                        tail_image = self.images["tail"]
                    elif x[1] < next_pos[1]:
                        tail_image = pygame.transform.rotate(self.images["tail"], 90)
                    else:
                        tail_image = pygame.transform.rotate(self.images["tail"], -90)
                    dis.blit(tail_image, (x[0], x[1]))
            else:
                # Rotate body image based on direction
                prev_pos = self.positions[i - 1]
                next_pos = self.positions[i + 1]
                if prev_pos[0] == next_pos[0]:
                    body_image = pygame.transform.rotate(self.images["body"], 90)
                elif prev_pos[1] == next_pos[1]:
                    body_image = self.images["body"]
                else:
                    if (prev_pos[0] < x[0] and next_pos[1] < x[1]) or (
                        next_pos[0] < x[0] and prev_pos[1] < x[1]
                    ):
                        body_image = pygame.transform.rotate(self.images["turn"], +90)
                    elif (prev_pos[0] < x[0] and next_pos[1] > x[1]) or (
                        next_pos[0] < x[0] and prev_pos[1] > x[1]
                    ):
                        body_image = pygame.transform.rotate(self.images["turn"], 180)
                    elif (prev_pos[0] > x[0] and next_pos[1] < x[1]) or (
                        next_pos[0] > x[0] and prev_pos[1] < x[1]
                    ):
                        body_image = pygame.transform.rotate(self.images["turn"], 0)
                    else:
                        body_image = pygame.transform.rotate(self.images["turn"], -90)
                dis.blit(body_image, (x[0], x[1]))

    def show_score(self, dis, font, prefix="", color=(255, 255, 102)):
        """Display the current score on the screen."""
        value = font.render(prefix + str(self.score), True, color)
        dis.blit(value, [0, 0])

    def update(self):
        self.positions.append(self.head.copy())
        if len(self.positions) > self.length:
            del self.positions[0]

    def handle(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            return Direction.LEFT
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            return Direction.RIGHT
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            return Direction.UP
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            return Direction.DOWN
        return Direction.STILL

    def out_of_bounds(self, dis_width, dis_height):
        return (
            self.head[0] >= dis_width
            or self.head[0] < 0
            or self.head[1] >= dis_height
            or self.head[1] < 0
        )

    def self_collision(self):
        """
        Check if the snake has collided with itself.
        Returns True if a collision is detected, otherwise False.
        """
        for pos in self.positions[:-1]:
            if pos == self.head:
                return True
        return False

    def grow(self):
        self.length += 1

    def shrink(self):
        """
        Halve the snake's length, ensuring it doesn't go below 1.
        Returns True if the snake's length is now 1 or less, indicating game over.
        """
        self.length = max(1, self.length // 2)
        # Reduce the positions list to match the new length
        self.positions = self.positions[-self.length:]
        return self.length <= 1

    def move(self, direction):
        self.direction = direction
        x_change, y_change = Snake.delta(direction)
        self.head[0] += x_change
        self.head[1] += y_change

    def collide(self, x, y):
        return self.head[0] == x and self.head[1] == y

    @staticmethod
    def delta(direction):
        if direction == Direction.UP:
            return [0, -Snake.BLOCK]
        elif direction == Direction.DOWN:
            return [0, Snake.BLOCK]
        elif direction == Direction.LEFT:
            return [-Snake.BLOCK, 0]
        elif direction == Direction.RIGHT:
            return [Snake.BLOCK, 0]
        return [0, 0]
