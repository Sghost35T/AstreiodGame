import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        speed = 200  # pixels per second
        if keys[pygame.K_LEFT]:
            self.position.x -= speed * dt
        if keys[pygame.K_RIGHT]:
            self.position.x += speed * dt

    def collides(self, other):
        return self.position.distance_to(other.position) < (self.radius + other.radius)